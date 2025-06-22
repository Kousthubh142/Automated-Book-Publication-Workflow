import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")  

def review_chapter(spun_text: str, original_text: str) -> str:
    prompt = f"""You are a reviewer. Compare the rewritten (spun) text with the original.
Your goal is to make sure:
- The meaning is preserved
- The grammar and clarity are improved
- Any factual errors are corrected

Original:
{original_text}

Rewritten:
{spun_text}

Now refine the rewritten version accordingly.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "[Error during review]"
