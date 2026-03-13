from config import GEMINI_API_KEY
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_medical_chatbot(question, labs):

    prompt = f"""
You are a medical assistant helping a patient understand their lab report.

Lab Results:
{labs}

Patient Question:
{question}

Provide a simple explanation in easy language.
Do not give strict medical diagnosis.
Encourage consulting a doctor if needed.
"""

    response = model.generate_content(prompt)

    return response.text