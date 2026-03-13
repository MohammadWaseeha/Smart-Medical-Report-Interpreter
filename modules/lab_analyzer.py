
import re

reference_tests = [
"glucose","hemoglobin","hb","wbc","rbc","platelets",
"cholesterol","hdl","ldl","triglycerides",
"creatinine","bilirubin","tsh","urea",
"sodium","potassium","calcium"
]

def clean_text(text):

    text = text.lower()
    text = text.replace(",", "")
    return text

def extract_lab_values(text):

    text = clean_text(text)

    labs = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Pattern for table rows
        match = re.search(r"([a-zA-Z %]+)\s+(\d+\.?\d*)\s*([a-zA-Z/%^0-9]*)", line)

        if match:

            test = match.group(1).strip()
            value = match.group(2)
            unit = match.group(3)

            for ref in reference_tests:

                if ref in test:

                    labs.append({
                        "test": ref,
                        "value": float(value),
                        "unit": unit
                    })

                    break

    return labs