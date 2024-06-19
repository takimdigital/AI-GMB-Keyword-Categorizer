import pandas as pd
from openai import OpenAI
import json

# Initialize the OpenAI client
client = OpenAI(base_url="http://localhost:12345/v1", api_key="lm-studio")

# Load the CSV file
data = pd.read_csv('C://Users//Takim//Downloads//full_list_Google_Business_Profile.csv')

# Ensure the columns are set to accept any type of data
data['category'] = data['category'].astype('object')
data['Subcategory'] = data['Subcategory'].astype('object')

# Ask user for the maximum number of rows to process
max_rows = int(input("Enter the maximum number of rows to process: "))

# Loop over each row in the DataFrame
for index, row in data.iterrows():
    if index >= max_rows:
        break  # Limit processing based on user input

    keyword = row['GMB KEYWORD']
    
    # Generate the category and subcategory for the keyword
    completion = client.chat.completions.create(
        model="mradermacher/bophades-v2-mistral-7B-GGUF",
        messages=[
            {"role": "system", "content": "Category Identification|Action: Use analyze the GMB keyword and classify the business into a specific category (e.g., healthcare, retail, hospitality, etc.).Subcategory Identification|Action:refine the category into subcategories (e.g., for healthcare: dental, medical clinic, physiotherapy, etc)."},
            {"role": "user", "content": f"Write the appropriate category and subcategory for the following GMB keyword, and output the information in JSON format:\n\nKeyword: {keyword}"}
        ],
        temperature=0.7,
    )
    
    # Extract the response and update the DataFrame
    response_json = completion.choices[0].message.content
    try:
        result = json.loads(response_json)
        category = result['Category']
        subcategory = result['Subcategory']

        # Update the DataFrame
        data.at[index, 'category'] = category
        data.at[index, 'Subcategory'] = subcategory
        print(f"Updated row {index} with Category: {category} and Subcategory: {subcategory}")

    except json.JSONDecodeError:
        print(f"Failed to parse JSON for keyword '{keyword}'. Response was: {response_json}")
    except KeyError:
        print(f"JSON response does not contain 'Category' or 'Subcategory' fields. Response was: {response_json}")

# Save the updated DataFrame back to a CSV file
data.to_csv('C://Users//Takim//Downloads//updated_GMB_keywords.csv', index=False)
print("CSV file has been updated and saved.")