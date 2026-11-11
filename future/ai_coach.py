"""
Zecpath AI
Day 58 - AI Coaching Engine
"""

def generate_feedback(scores):
    """
    Generate personalized candidate improvement suggestions.
    """

    feedback = []

    if scores.get("communication", 0) < 70:
        feedback.append("Improve communication clarity.")

    if scores.get("technical", 0) < 70:
        feedback.append("Strengthen technical fundamentals.")

    if scores.get("confidence", 0) < 65:
        feedback.append("Work on confidence and interview delivery.")

    if scores.get("behavior", 100) < 70:
        feedback.append("Maintain better focus during interviews.")

    if not feedback:
        feedback.append("Excellent performance. Continue practicing advanced interview scenarios.")

    return feedback


if __name__ == "__main__":
    scores = {
        "communication": 60,
        "technical": 80,
        "confidence": 55,
        "behavior": 75
    }

    print(generate_feedback(scores))