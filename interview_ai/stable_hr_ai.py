"""
Stable HR Interview AI
Zecpath AI
"""

# -------------------------------
# DECISION THRESHOLDS
# -------------------------------
DECISION_THRESHOLDS = {

    "hire": 75,

    "consider": 55
}


# -------------------------------
# SMOOTH SCORES
# -------------------------------
def smooth_score(scores):

    if not scores:

        return 0

    avg = sum(scores) / len(scores)

    filtered = [

        s

        for s in scores

        if abs(s - avg) <= 20
    ]

    if filtered:

        return round(

            sum(filtered)

            / len(filtered),

            2
        )

    return round(avg, 2)


# -------------------------------
# STABLE DECISION
# -------------------------------
def stable_decision(score):

    if score >= DECISION_THRESHOLDS["hire"]:

        return "Hire"

    elif score >= DECISION_THRESHOLDS["consider"]:

        return "Consider"

    return "Reject"


# -------------------------------
# FINAL EVALUATION
# -------------------------------
def stable_hr_evaluation(scores):

    smoothed = smooth_score(scores)

    decision = stable_decision(smoothed)

    return {

        "stable_score":

            smoothed,

        "decision":

            decision
    }


if __name__ == "__main__":

    print(

        stable_hr_evaluation(

            [50, 60, 90, 30]

        )
    )