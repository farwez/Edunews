import requests
import os
from config import GROQ_API_KEY

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def summarize_text(text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Summarize news in 1-2 sentences in a catchy, professional tone."},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    
    # Safe extraction
    try:
        summary = result['choices'][0]['message']['content']
    except (KeyError, IndexError):
        summary = text  # fallback: use original text
    return summary

