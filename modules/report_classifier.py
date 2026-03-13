
def detect_report_type(text):

    text = text.lower()

    # Radiology keywords
    radiology_keywords = [
        "impression",
        "findings",
        "ct scan",
        "mri",
        "x-ray",
        "ultrasound",
        "radiology",
        "scan shows",
        "no evidence of",
        "lesion",
        "fracture"
    ]

    # Lab report keywords
    lab_keywords = [
        "hemoglobin",
        "glucose",
        "cholesterol",
        "platelets",
        "wbc",
        "rbc",
        "triglycerides",
        "hdl",
        "ldl",
        "bilirubin",
        "creatinine",
        "tsh",
        "mg/dl",
        "g/dl",
        "mmol/l"
    ]

    # Prescription keywords
    prescription_keywords = [
        "tablet",
        "capsule",
        "dosage",
        "take once daily",
        "take twice daily",
        "prescription",
        "after food",
        "before food"
    ]

    # Radiology detection
    for word in radiology_keywords:
        if word in text:
            return "Radiology Report"

    # Lab detection
    for word in lab_keywords:
        if word in text:
            return "Lab Report"

    # Prescription detection
    for word in prescription_keywords:
        if word in text:
            return "Prescription"

    return "General Medical Report"