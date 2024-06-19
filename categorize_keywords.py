import pandas as pd
from openai import OpenAI
import json
import os   

# Initialize the OpenAI client
client = OpenAI(base_url="http://localhost:12345/v1", api_key="lm-studio")

# Define the file paths
base_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_path, 'full_list_Google_Business_Profile.csv')
output_file = os.path.join(base_path, 'updated_GMB_keywords.csv')

# Load the CSV file
data = pd.read_csv(input_file)

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
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant specializing in business categorization. "
                        "Your task is to analyze the given Google My Business (GMB) keyword and classify the business into "
                        "the most appropriate category and subcategory. Use the following guidelines:\n"
                        "1. Category Identification: Identify the primary category that best represents the business type (e.g., healthcare, retail, hospitality, etc.).\n"
                        "2. Subcategory Identification: Further refine the primary category into specific subcategories (e.g., for healthcare: dental, medical clinic, physiotherapy, etc.).\n"
                        "Output the result in JSON format with 'Category' and 'Subcategory' keys."
                    )
                },
                {
                    "role": "user",
                    "content": f"Write the appropriate category and subcategory for the following GMB keyword, and output the information in JSON format:\n\nKeyword: {keyword}"
                }
            ],
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
data.to_csv(output_file, index=False)
print("CSV file has been updated and saved.")
