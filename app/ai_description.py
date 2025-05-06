import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
MODEL = "meta-llama/Llama-3.1-8B-Instruct"

def generate_description(item_name):
    prompt = f"Write a product description under 100 words for a second-hand {item_name} in good condition."

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{MODEL}",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"⚠️ Error from Hugging Face: {response.status_code} - {response.text}"