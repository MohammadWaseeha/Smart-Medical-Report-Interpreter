import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def simplify_radiology(text):

    prompt = f"""
Explain this radiology report in simple language
so a patient with no medical knowledge can understand.

Give:
• Key findings
• Possible meaning
• When to consult a doctor

Radiology Report:
{text}
"""

    response = model.generate_content(prompt)

    return response.text