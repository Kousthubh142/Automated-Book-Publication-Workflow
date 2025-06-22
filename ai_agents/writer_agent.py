import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")  

def spin_chapter(text: str, temperature: float = 0.7) -> str:
    prompt = f"""Rewrite the following chapter in a more modern, engaging style. Do not change the meaning, but make the language easier to read:

{text}
"""
    try:
        response = model.generate_content(
            prompt,
            generation_config={"temperature": temperature}
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "[Error generating content]"
