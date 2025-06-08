import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash")

def generate_response(user_input: str) -> str:
    prompt = f"You are a Socratic tutor. Respond with thoughtful questions to: {user_input}"
    response = model.generate_content(prompt)
    return response.text.strip()
