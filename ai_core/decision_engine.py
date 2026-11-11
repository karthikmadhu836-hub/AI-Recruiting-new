"""
Decision AI Engine
Zecpath AI
"""

# ----------------------------------------
# Decision Thresholds
# ----------------------------------------

THRESHOLDS = {

    "selected": 80,

    "hold": 60

}


# ----------------------------------------
# Risk Adjustment
# ----------------------------------------

def adjust_for_risk(

    score,

    behavior_risk="Low Risk",

    integrity_risk="Low Risk"

):

    penalty = 0

    if behavior_risk == "High Risk":

        penalty += 10

    elif behavior_risk == "Moderate Risk":

        penalty += 5

    if integrity_risk == "High Risk":

        penalty += 15

    elif integrity_risk == "Moderate Risk":

        penalty += 7

    return max(score - penalty, 0)


# ----------------------------------------
# Decision Logic
# ----------------------------------------

def generate_decision(

    final_score,

    behavior_risk="Low Risk",

    integrity_risk="Low Risk"

):

    adjusted_score = adjust_for_risk(

        final_score,

        behavior_risk,

        integrity_risk

    )

    if adjusted_score >= THRESHOLDS["selected"]:

        decision = "Selected"

    elif adjusted_score >= THRESHOLDS["hold"]:

        decision = "Hold / Review"

    else:

        decision = "Rejected"

    return decision, adjusted_score


# ----------------------------------------
# Confidence Score
# ----------------------------------------

def calculate_decision_confidence(scores):

    if not scores:

        return 0

    variance = max(scores) - min(scores)

    confidence = max(100 - variance, 50)

    return round(confidence, 2)


# ----------------------------------------
# Explainable Output
# ----------------------------------------

def generate_explanation(

    scores,

    decision

):

    strengths = []

    weaknesses = []

    if scores.get("technical", 0) >= 80:

        strengths.append("Strong technical skills")

    if scores.get("communication", 0) >= 75:

        strengths.append("Good communication")

    if scores.get("behavior", 100) < 60:

        weaknesses.append("Behavioral concerns")

    if scores.get("integrity", 100) < 60:

        weaknesses.append("Integrity risks")

    return {

        "decision": decision,

        "strengths": strengths,

        "weaknesses": weaknesses

    }


# ----------------------------------------
# Example
# ----------------------------------------

if __name__ == "__main__":

    decision, score = generate_decision(

        85,

        "Low Risk",

        "Moderate Risk"

    )

    print(decision)

    print(score)