import pandas as pd
from openai import OpenAI
import json

# Initialize the OpenAI client
client = OpenAI(base_url="http://localhost:12345/v1", api_key="your_api_key")

# Load the enriched CSV file
data = pd.read_csv('C://Users//Takim//Downloads//updated_GMB_keywords.csv')

# Define the new columns
columns = [
    'Cleaning Frequency', 'Special Cleaning Requirements', 'Potential Customer Pain Points', 
    'Suggested Marketing Messages', 'Service Packages', 'Cost Estimates', 
    'Competitive Advantages', 'Compliance Requirements', 'Quality Standards', 'Health & Safety Tips'
]

# Ensure the columns are set to accept any type of data
for column in columns:
    data[column] = data[column].astype('object')

# Ask user for the maximum number of rows to process
max_rows = int(input("Enter the maximum number of rows to process: "))

# Function to generate foundational content
def generate_foundational_content(keyword, category, subcategory):
    completion = client.chat.completions.create(
        model="mradermacher/bophades-v2-mistral-7B-GGUF",
        messages=[
            {"role": "system", "content": "You are an AI assistant providing detailed content for a cleaning company targeting specific business types. Generate comprehensive, practical, and relevant content based on industry best practices and local SEO optimization."},
            {"role": "user", "content": f"Based on the GMB keyword '{keyword}', category '{category}', and subcategory '{subcategory}', provide the following information in JSON format:\n\n"
                                        f"Cleaning Frequency: What is the recommended cleaning frequency for this business type?\n"
                                        f"Special Cleaning Requirements: List any special cleaning needs or considerations specific to this business type.\n"
                                        f"Potential Customer Pain Points: Identify common issues or pain points customers in this business type face regarding cleanliness and maintenance.\n"
                                        f"Suggested Marketing Messages: Provide effective marketing messages that can attract businesses in this category. Include language that emphasizes unique selling points and customer benefits.\n"
                                        f"Service Packages: Describe suggested cleaning service packages, including names, detailed descriptions, and what each package entails.\n"
                                        f"Cost Estimates: Provide average cost estimates for each cleaning service package offered.\n"
                                        f"Competitive Advantages: Highlight unique selling points or competitive advantages that make your cleaning services stand out for this business type.\n"
                                        f"Compliance Requirements: List any specific compliance or regulatory requirements related to cleanliness and maintenance for this business type.\n"
                                        f"Quality Standards: Define the standards of quality that need to be met to ensure customer satisfaction and regulatory compliance.\n"
                                        f"Health & Safety Tips: Offer health and safety tips specific to maintaining a clean and safe environment for this business type."}
        ],
        temperature=0.7,
    )
    return completion.choices[0].message.content

# Loop over each row in the DataFrame
for index, row in data.iterrows():
    if index >= max_rows:
        break  # Limit processing based on user input

    # Check if new columns already have data
    if any(pd.notnull(row[column]) for column in columns):
        print(f"Skipping row {index} as it already contains data in one of the new columns")
        continue

    keyword = row['GMB KEYWORD']
    category = row['category']
    subcategory = row['Subcategory']
    
    if pd.isnull(category) or pd.isnull(subcategory):
        print(f"Skipping row {index} due to missing category or subcategory")
        continue
    
    # Generate foundational content
    try:
        response_json = generate_foundational_content(keyword, category, subcategory)
        result = json.loads(response_json)
        
        # Verify the JSON contains all required keys and update the DataFrame
        for column in columns:
            data.at[index, column] = result.get(column, 'N/A')
        print(f"Updated row {index} with foundational content.")
        
    except json.JSONDecodeError:
        print(f"Failed to parse JSON for keyword '{keyword}'. Response was: {response_json}")
    except KeyError:
        print(f"JSON response does not contain all required fields. Response was: {response_json}")

# Save the updated DataFrame back to a CSV file
data.to_csv('C://Users//Takim//Downloads//foundational_content_GMB_keywords_updated.csv', index=False)
print("CSV file has been updated and saved.")
