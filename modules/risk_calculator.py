reference_ranges = {

"glucose": (70,100),
"hemoglobin": (13,17),
"wbc": (4000,11000),
"rbc": (4.5,6),
"platelets": (150000,450000),
"cholesterol": (0,200),
"ldl": (0,100),
"hdl": (40,60),
"triglycerides": (0,150),
"creatinine": (0.7,1.3),
"tsh": (0.4,4.0),
"bilirubin": (0.1,1.2)

}

# Medical importance weight
test_weights = {

"glucose":3,
"cholesterol":3,
"ldl":3,
"hdl":2,
"triglycerides":2,
"hemoglobin":2,
"wbc":2,
"rbc":1,
"platelets":1,
"creatinine":3,
"tsh":2,
"bilirubin":2

}

def analyze_labs(labs):

    findings=[]
    score=0

    for lab in labs:

        test=lab["test"].lower()
        value=lab["value"]

        if test in reference_ranges:

            low,high=reference_ranges[test]
            weight=test_weights.get(test,1)

            if value < low:
                findings.append((test,"Low","⚠"))
                score+=1*weight

            elif value > high:
                findings.append((test,"High","⚠"))
                score+=1*weight

            else:
                findings.append((test,"Normal","✓"))

    return findings,score


def risk_level(score):

    if score <=3:
        return "Low"

    elif score <=7:
        return "Medium"

    else:
        return "High"