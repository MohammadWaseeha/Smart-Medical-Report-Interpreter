doctor_map = {

"glucose":"Endocrinologist",
"tsh":"Endocrinologist",
"cholesterol":"Cardiologist",
"ldl":"Cardiologist",
"hdl":"Cardiologist",
"triglycerides":"Cardiologist",
"hemoglobin":"Hematologist",
"wbc":"Hematologist",
"rbc":"Hematologist",
"platelets":"Hematologist",
"creatinine":"Nephrologist",
"bilirubin":"Gastroenterologist"

}

def recommend_doctor(findings):

    doctors=[]

    for test,status,_ in findings:

        if status!="Normal":

            doctor=doctor_map.get(test)

            if doctor:
                doctors.append(doctor)

    if doctors:

        return list(set(doctors))[0]

    return "General Physician"