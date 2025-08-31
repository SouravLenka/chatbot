OMEN – AI Chatbot by Sourav Lenka

OMEN is a sleek, interactive AI chatbot powered by OpenAI’s GPT-4o-mini. Built with Streamlit, it lets you chat with an intelligent assistant in real-time, directly in your browser or locally.

💻 Live Demo: OMEN on Streamlit Cloud

✨ Features

Real-time conversational AI powered by GPT-4o-mini

Clean and minimal web interface using Streamlit

Stores chat history during your session

Easy to set up and run locally

Works seamlessly online via Streamlit Cloud

⚡ Installation

Clone the repository:

git clone https://github.com/SouravLenka/omen-chatbot.git


Navigate to the project folder:

cd omen-chatbot


Create a virtual environment (optional but recommended):

python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate


Install dependencies:

pip install -r requirements.txt

🔑 Setup

Get your OpenAI API key from OpenAI
.

Create a .streamlit/secrets.toml file:

[general]
OPENAI_API_KEY = "your_openai_api_key_here"

🚀 Usage

Run the chatbot locally:

streamlit run app.py


Type your queries in the input box, and OMEN will respond instantly using GPT-4o-mini.

🛠 Technologies Used

Python

Streamlit

OpenAI GPT-4o-mini
