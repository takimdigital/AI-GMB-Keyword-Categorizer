import pandas as pd
from openai import OpenAI
import json
import os

# Initialize the OpenAI client
client = OpenAI(base_url="http://localhost:12345/v1", api_key="your_api_key")

# Define the file paths
base_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_path, 'updated_GMB_keywords.csv')
output_file = os.path.join(base_path, 'foundational_content_GMB_keywords_updated.csv')

# Load the enriched CSV file
data = pd.read_csv(input_file)

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
            {
                "role": "system",
                "content": (
                    "You are an AI assistant providing detailed and practical content for a cleaning company "
                    "targeting specific business types. Your responses should be comprehensive, practical, and relevant, "
                    "based on industry best practices and local SEO optimization. Each response must include actionable insights "
                    "and be tailored to the specific business type identified by the GMB keyword, category, and subcategory."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Based on the GMB keyword '{keyword}', category '{category}', and subcategory '{subcategory}', provide the following "
                    f"information in JSON format with concise and actionable insights. Use the exact structure provided:\n\n"
                    
                    "{\n"
                    "  \"Cleaning Frequency\": \"...\",\n"
                    "  \"Special Cleaning Requirements\": \"...\",\n"
                    "  \"Potential Customer Pain Points\": \"...\",\n"
                    "  \"Suggested Marketing Messages\": \"...\",\n"
                    "  \"Service Packages\": {\n"
                    "    \"Basic\": {\n"
                    "      \"Description\": \"...\",\n"
                    "      \"Benefits\": \"...\"\n"
                    "    },\n"
                    "    \"Premium\": {\n"
                    "      \"Description\": \"...\",\n"
                    "      \"Benefits\": \"...\"\n"
                    "    }\n"
                    "  },\n"
                    "  \"Cost Estimates\": {\n"
                    "    \"Basic\": \"...\",\n"
                    "    \"Premium\": \"...\"\n"
                    "  },\n"
                    "  \"Competitive Advantages\": \"...\",\n"
                    "  \"Compliance Requirements\": \"...\",\n"
                    "  \"Quality Standards\": \"...\",\n"
                    "  \"Health & Safety Tips\": \"...\"\n"
                    "}"
                )
            }
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
        try:
            result = json.loads(response_json)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON for keyword '{keyword}'. Response was: {response_json}. Error: {e}")
            continue
        
        # Verify the JSON contains all required keys and update the DataFrame
        for column in columns:
            data.at[index, column] = result.get(column, 'N/A')
        print(f"Updated row {index} with foundational content.")
        
    except Exception as e:
        print(f"An error occurred for keyword '{keyword}'. Error: {e}")

# Save the updated DataFrame back to a CSV file
data.to_csv(output_file, index=False)
print("CSV file has been updated and saved.")
