"""
Behavior Signal Mapping Model
Zecpath AI
"""

# ----------------------------------------
# Behavior Score Calculation
# ----------------------------------------
def calculate_behavior_score(signals):
    """
    Expected input:

    {
        "eye_focus":0-1,
        "head_stability":0-1,
        "engagement":0-1,
        "distraction":0-1
    }
    """

    focus = signals.get(
        "eye_focus",
        0.5
    )

    head = signals.get(
        "head_stability",
        0.5
    )

    engagement = signals.get(
        "engagement",
        0.5
    )

    distraction = signals.get(
        "distraction",
        0.5
    )

    score = (

        focus * 0.30 +

        head * 0.20 +

        engagement * 0.30 +

        (1 - distraction) * 0.20

    )

    return round(score * 100, 2)


# ----------------------------------------
# Behavioral Level
# ----------------------------------------
def behavior_level(score):

    if score >= 85:
        return "Highly Focused"

    elif score >= 70:
        return "Good Engagement"

    elif score >= 50:
        return "Moderate"

    return "Distracted"


# ----------------------------------------
# Risk Detection
# ----------------------------------------
def detect_behavior_risk(score):

    if score < 50:
        return "High Risk"

    elif score < 70:
        return "Moderate Risk"

    return "Low Risk"


# ----------------------------------------
# Generate Insights
# ----------------------------------------
def generate_behavior_report(signals):

    score = calculate_behavior_score(signals)

    return {

        "behavior_score": score,

        "signals": signals,

        "insights": {

            "behavior_level":
                behavior_level(score),

            "risk":
                detect_behavior_risk(score)

        }

    }


# ----------------------------------------
# Example
# ----------------------------------------
if __name__ == "__main__":

    sample = {

        "eye_focus": 0.8,

        "head_stability": 0.7,

        "engagement": 0.9,

        "distraction": 0.2

    }

    print(
        generate_behavior_report(sample)
    )