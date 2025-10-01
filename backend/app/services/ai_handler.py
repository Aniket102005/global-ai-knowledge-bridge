import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Updated with information from the official hackathon documentation
CEREBRAS_API_URL = "https://api.cerebras.ai/v1/chat/completions" 
CEREBRAS_MODEL_NAME = "gpt-oss-120b" # Correct model from the docs

CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")

def summarize_text_with_cerebras(text_to_summarize: str) -> str:
    """
    Sends text to the Cerebras API in the correct chat format and returns a summary.
    """
    if not CEREBRAS_API_KEY:
        return "Error: CEREBRAS_API_KEY is not set."

    headers = {
        "Authorization": f"Bearer {CEREBRAS_API_KEY}",
        "Content-Type": "application/json",
    }

    # The API expects a 'model' and a 'messages' array.
    payload = {
        "model": CEREBRAS_MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": f"Please provide a concise summary of the following document:\n\n{text_to_summarize}"
            }
        ]
    }

    try:
        response = requests.post(CEREBRAS_API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            # The summary is inside the 'choices' array in the response.
            response_data = response.json()
            summary = response_data.get("choices", [{}])[0].get("message", {}).get("content", "Error: Summary not found in the response format.")
            return summary
        else:
            return f"Error: API request failed with status code {response.status_code} - {response.text}"
            
    except requests.exceptions.RequestException as e:
        return f"Error: An exception occurred while making the API request: {e}"

def get_answer_with_llama(context: str, question: str, language: str) -> str:
    """
    (Placeholder) Sends context and a question to Llama for an answer.
    """
    # This will be implemented next.
    return f"LLaMA's answer to '{question}' in {language} based on the context will go here."

