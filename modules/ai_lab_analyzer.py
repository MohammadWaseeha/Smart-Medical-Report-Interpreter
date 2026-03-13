import google.generativeai as genai
from config import GEMINI_API_KEY
import json

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_labs_with_ai(report_text):

    prompt = f"""
You are a medical report analyzer.

Extract all lab test results from the report.

Return ONLY JSON in this format:

[
  {{
    "test": "Glucose",
    "value": "92",
    "unit": "mg/dL"
  }}
]

Medical Report:
{report_text}
"""

    response = model.generate_content(prompt)

    try:
        labs = json.loads(response.text)
    except:
        labs = []

    return labs