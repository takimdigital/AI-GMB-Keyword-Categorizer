# GMB Keyword Categorizer and Content Generator
Harness the power of local AI to categorize and enrich Google My Business (GMB) keywords for cleaning companies.

## 📖 Overview
Welcome to the GMB Keyword Categorizer and Content Generator! This project utilizes local Large Language Models (LLMs) to categorize GMB keywords and generate comprehensive content for cleaning companies. It's a zero-cost alternative to cloud-based services, ensuring privacy and offline processing. I'm not a coder by profession – just someone passionate about leveraging AI for business improvement, sharing my journey of creating valuable insights for cleaning companies and beyond.

## 🌟 Features
- **Zero-Cost Categorization**: Utilize advanced AI capabilities without any cloud expenses.
- **Local LLM Utilization**: Everything runs on your machine, ensuring data privacy.
- **Comprehensive Content Generation**: Create detailed, practical content tailored to business types.
- **Customization at Heart**: Easily modify models and prompts to fit different business needs.
- **Human-Centric Design**: Built with simplicity in mind, from a non-developer's perspective.

## ✨ Motivation
This project was inspired by the need to classify and enrich GMB keywords efficiently. It's aimed at helping cleaning companies optimize their online presence and marketing strategies. With around 4000 GMB keywords, it took me 29 hours to process everything using my RTX 3070, amidst my children occasionally interrupting. There's always room for improvement, but this is a solid proof of concept.

## 🚀 Getting Started
Clone the repository:
```bash
git clone https://github.com/takimdigital/GMB-Keyword-Categorizer.git
```

Navigate to the project directory:
```bash
cd GMB-Keyword-Categorizer
```

Install dependencies (if any):
```bash
pip install -r requirements.txt
```

### Script 1: Categorize and Subcategorize GMB Keywords
Run the first script to categorize and subcategorize the GMB keywords:
```bash
python categorize_keywords.py
```

### Script 2: Generate Foundational Content
Run the second script to generate detailed content for the categorized keywords:
```bash
python generate_content.py
```

Follow the interactive prompts to process your CSV and generate insights.

## 🖊️ How to Modify
This project is tailored for cleaning companies, but if you need to adjust it for another business type, such as a marketing agency, you'll need to modify the prompts accordingly.

### CSV Information
Ensure your CSV file is formatted correctly with columns: `GMB KEYWORD`, `category`, and `Subcategory`.

### Modify Prompts
Update the prompts in the script to fit different business types or requirements.

#### Example for a Marketing Agency:
In `categorize_keywords.py`, change the prompt to reflect categories relevant to marketing:

```python
{"role": "system", "content": "Category Identification|Action: Use analyze the GMB keyword and classify the business into a specific category (e.g., digital marketing, content creation, SEO, etc.). Subcategory Identification|Action: refine the category into subcategories (e.g., for digital marketing: social media marketing, email marketing, PPC, etc)."}
```

In `generate_content.py`, update the prompt for generating foundational content specific to a marketing agency:

```python
{"role": "user", "content": f"Based on the GMB keyword '{keyword}', category '{category}', and subcategory '{subcategory}', provide the following information in JSON format:\n\nRecommended Marketing Strategies: What are the best marketing strategies for this business type?\nCommon Challenges: Identify common challenges this business type faces in marketing.\nSuggested Campaign Ideas: Provide effective campaign ideas to attract clients in this category.\nCompetitive Advantages: Highlight unique selling points or competitive advantages for this business type.\nIndustry Trends: List the latest trends in the marketing industry relevant to this business type.\nClient Pain Points: Identify common pain points clients face and how to address them.\nSuccess Metrics: Define key success metrics for marketing campaigns in this business type.\nCompliance Requirements: List any specific compliance or regulatory requirements related to marketing for this business type.\nBest Practices: Offer best practices for successful marketing campaigns.\nTools and Resources: Suggest useful tools and resources for marketing professionals in this business type."}
```

### Adjust Script Logic
To use another local LLM, such as Ollama, change the API client initialization and endpoints accordingly. For example:

```python
import ollama
client = ollama.Client(host='http://localhost:11434')
response = client.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
```

### Specific Example
In `generate_content.py`, update the prompt for generating foundational content:

```python
{"role": "user", "content": f"Based on the GMB keyword '{keyword}', category '{category}', and subcategory '{subcategory}', provide the following information in JSON format:\n\nRecommended Marketing Strategies: What are the best marketing strategies for this business type?\nCommon Challenges: Identify common challenges this business type faces in marketing.\nSuggested Campaign Ideas: Provide effective campaign ideas to attract clients in this category.\nCompetitive Advantages: Highlight unique selling points or competitive advantages for this business type.\nIndustry Trends: List the latest trends in the marketing industry relevant to this business type.\nClient Pain Points: Identify common pain points clients face and how to address them.\nSuccess Metrics: Define key success metrics for marketing campaigns in this business type.\nCompliance Requirements: List any specific compliance or regulatory requirements related to marketing for this business type.\nBest Practices: Offer best practices for successful marketing campaigns.\nTools and Resources: Suggest useful tools and resources for marketing professionals in this business type."}
```

## 📜 Use Case: Tailored Cleaning Company Marketing
This project is tailored to help cleaning companies generate detailed marketing content based on their GMB keywords. For example, if your GMB keyword is "Dental Clinic Cleaning", the script will categorize it under "Healthcare" and subcategorize it as "Dental". The foundational content generated will include cleaning frequencies, special requirements, marketing messages, service packages, and more, specific to dental clinics.

### Example Output
For a GMB keyword like "Dental Clinic Cleaning", you might get:
- **Cleaning Frequency**: Daily for high-traffic areas, weekly for others.
- **Special Cleaning Requirements**: Use of disinfectants approved for medical facilities.
- **Potential Customer Pain Points**: Concern about the sterility of instruments and surfaces.
- **Suggested Marketing Messages**: "Ensure the highest level of cleanliness and safety for your patients."
- **Service Packages**: Basic, Standard, Premium with detailed descriptions.
- **Cost Estimates**: Average costs for each package.
- **Competitive Advantages**: Specialized in healthcare cleaning with trained staff.
- **Compliance Requirements**: Adherence to health and safety regulations.
- **Quality Standards**: High standards to meet medical facility requirements.
- **Health & Safety Tips**: Regular disinfection of high-touch areas.

## 🚀 Next Improvements
For future improvements, I plan to:
- **Synchronization**: Add asynchronous processing to improve efficiency.
- **Model Selection**: Provide a list of local LMs to choose and switch between models.
- **Error Handling**: Enhance error handling to catch and manage specific exceptions.
- **User Interface**: Develop a UI for easier interaction and configuration.
- **AI Agent for Dynamic Excel Updates**: Implement an AI agent to automatically create and update the Excel file based on user queries and needs.

## 👐 Contributing
Your ideas and contributions are welcome! Whether it's suggesting features, reporting bugs, or improving documentation, your help is appreciated. Feel free to fork the repository and submit pull requests.

## 📜 License
This project is open-source and available under the Apache 2.0 License. Use it, modify it, share it – but remember to attribute!

## 🙌 Acknowledgments
A big thanks to [LM Studio](https://lmstudio.ai/) for their local LLMs, and to the open-source community for the inspiration and support. Also, consider exploring [Ollama](https://ollama.com/) for alternative LLM options.

## 📬 Get in Touch!
Have suggestions? Found a way to improve this project? I'd love to hear from you. Reach out and let's make AI work for business improvement together!
```
