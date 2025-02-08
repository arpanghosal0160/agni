import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

def answer_question(query):
    try:
        response = co.generate(
            model='command-xlarge',
            prompt=query,
            max_tokens=100
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
