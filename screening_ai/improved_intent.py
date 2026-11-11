# -------------------------------
# Improved Intent Keywords
# -------------------------------
INTENT_KEYWORDS = {
    "experience": [
        "experience",
        "worked",
        "years",
        "role",
        "project"
    ],

    "skills": [
        "skills",
        "tools",
        "technologies",
        "stack"
    ],

    "salary": [
        "salary",
        "ctc",
        "expected",
        "pay"
    ],

    "availability": [
        "join",
        "notice",
        "immediate"
    ],

    "introduction": [
        "introduce",
        "background",
        "about"
    ]
}


# -------------------------------
# Improved Intent Classification
# -------------------------------
def improved_intent_classification(text):

    text = text.lower()

    scores = {}

    for intent, words in INTENT_KEYWORDS.items():

        scores[intent] = sum(
            word in text for word in words
        )

    best_intent = max(scores, key=scores.get)

    return best_intent if scores[best_intent] > 0 else "unknown"


# -------------------------------
# Improved Scoring Thresholds
# -------------------------------
DECISION_THRESHOLDS = {
    "pass": 65,
    "review": 45
}


def get_decision(score):

    if score >= DECISION_THRESHOLDS["pass"]:
        return "Pass"

    elif score >= DECISION_THRESHOLDS["review"]:
        return "Review"

    return "Reject"


# -------------------------------
# Example Execution
# -------------------------------
if __name__ == "__main__":

    text = "I worked as a backend developer for 2 years"

    intent = improved_intent_classification(text)

    print("Detected Intent:", intent)

    print("Decision for score 70:", get_decision(70))