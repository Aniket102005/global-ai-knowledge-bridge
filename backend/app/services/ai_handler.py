import os
import requests
from dotenv import load_dotenv

load_dotenv()

# --- Cerebras Configuration ---
CEREBRAS_API_URL = "https://api.cerebras.ai/v1/chat/completions"
CEREBRAS_MODEL_NAME = "gpt-oss-120b"
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")

# --- OpenRouter Configuration (for Llama) ---
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
LLAMA_MODEL_NAME = "meta-llama/llama-3-8b-instruct"

def summarize_text_with_cerebras(text_to_summarize: str) -> str:
    # This function is working perfectly.
    if not CEREBRAS_API_KEY:
        return "Error: CEREBRAS_API_KEY is not set."
    headers = {"Authorization": f"Bearer {CEREBRAS_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": CEREBRAS_MODEL_NAME, "messages": [{"role": "user", "content": f"Please provide a concise summary of the following document:\n\n{text_to_summarize}"}]}
    try:
        response = requests.post(CEREBRAS_API_URL, headers=headers, json=payload, timeout=120)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error: Summary not found.")
        else:
            return f"Error: API failed with status {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: An exception occurred: {e}"


def get_answer_with_llama(context: str, question: str, language: str) -> str:
    """
    Sends document context and a user's question to Llama 3 with a stricter prompt.
    """
    if not OPENROUTER_API_KEY:
        return "Error: OPENROUTER_API_KEY is not set in your .env file."

    # --- THIS IS THE NEW, IMPROVED PROMPT ---
    prompt = f"""
    You are an expert assistant. Your task is to answer the user's question based *only* on the provided text.
    Your entire response must be in simple, clear {language}. 
    Do not use any other languages. Do not mix languages.

    Provided Text:
    ---
    {context}
    ---

    User's Question: "{question}"
    """
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": LLAMA_MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=120)
        
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error: Could not get a response from Llama on OpenRouter.")
        else:
            return f"Error: OpenRouter API failed with status {response.status_code} - {response.text}"
            
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to OpenRouter. Details: {e}"
