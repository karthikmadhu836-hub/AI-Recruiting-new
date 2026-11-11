"""
Technical Skill Scoring Engine
Zecpath AI
"""

# -------------------------------
# Depth Detection
# -------------------------------
def detect_depth(text):
    keywords = [
        "because",
        "architecture",
        "optimize",
        "scalable",
        "tradeoff",
        "performance",
        "design",
        "system"
    ]

    count = sum(
        word in text.lower()
        for word in keywords
    )

    if count >= 4:
        return 1.0
    elif count >= 2:
        return 0.7
    return 0.4


# -------------------------------
# Logical Reasoning Score
# -------------------------------
def logical_score(text):

    text = text.lower()

    if "first" in text and "then" in text:
        return 1.0

    elif len(text.split()) > 15:
        return 0.7

    return 0.4


# -------------------------------
# Real World Applicability
# -------------------------------
def real_world_score(text):

    text = text.lower()

    if (
        "production" in text
        or "real-world" in text
        or "deployment" in text
    ):
        return 1.0

    elif (
        "example" in text
        or "project" in text
    ):
        return 0.7

    return 0.4


# -------------------------------
# Accuracy Score
# -------------------------------
def accuracy_score(is_correct):

    return 1.0 if is_correct else 0.4


# -------------------------------
# Difficulty Normalization
# -------------------------------
def normalize_difficulty(
    score,
    difficulty
):

    multipliers = {
        "basic": 1.0,
        "intermediate": 1.10,
        "advanced": 1.20
    }

    adjusted = score * multipliers.get(
        difficulty,
        1.0
    )

    return min(round(adjusted, 2), 100)


# -------------------------------
# Answer Depth Classification
# -------------------------------
def classify_answer_depth(text):

    words = len(text.split())

    if words > 20 and "because" in text.lower():
        return "Deep"

    elif words > 10:
        return "Moderate"

    return "Shallow"


# -------------------------------
# Main Technical Score
# -------------------------------
def calculate_technical_score(
    answer,
    difficulty="basic",
    is_correct=True
):

    depth = detect_depth(answer)

    logic = logical_score(answer)

    real_world = real_world_score(answer)

    accuracy = accuracy_score(is_correct)

    raw_score = (
        accuracy * 0.35 +
        depth * 0.25 +
        logic * 0.20 +
        real_world * 0.20
    ) * 100

    final_score = normalize_difficulty(
        raw_score,
        difficulty
    )

    return {

        "technical_score": final_score,

        "depth": classify_answer_depth(answer),

        "breakdown": {

            "accuracy": round(accuracy, 2),

            "depth": round(depth, 2),

            "logic": round(logic, 2),

            "real_world": round(real_world, 2)
        }
    }


# -------------------------------
# Example
# -------------------------------
if __name__ == "__main__":

    answer = (
        "First I design the architecture, "
        "then optimize performance because "
        "production systems need scalability."
    )

    print(
        calculate_technical_score(
            answer,
            "advanced",
            True
        )
    )