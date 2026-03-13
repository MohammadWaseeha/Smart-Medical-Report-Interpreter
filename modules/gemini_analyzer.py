import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_medical_summary(text):

    prompt = f"""
You are a medical assistant.

Analyze the following medical report text and produce:

1. Risk Level (Low / Medium / High)
2. Recommended Doctor
3. Doctor Visit Urgency (Routine / Soon / Immediate)
4. Health explanation in 3–4 simple bullet points for a non-medical person.

Medical Report:
{text}

Return response in this format:

Risk Level:
Recommended Doctor:
Urgency:
Explanation:
"""

    response = model.generate_content(prompt)

    return response.text