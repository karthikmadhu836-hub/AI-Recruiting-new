"""
Zecpath AI
Day 54 - Refined Scoring Logic
"""


# ---------------------------------
# Consistency Adjustment
# ---------------------------------

def consistency_adjustment(scores):

    values = list(scores.values())

    if not values:
        return 0

    variance = max(values) - min(values)

    # Penalize inconsistent performance
    if variance > 30:
        return -5

    # Reward consistency
    elif variance < 10:
        return 5

    return 0


# ---------------------------------
# Final Refined Score
# ---------------------------------

def refined_final_score(scores, base_score):

    adjustment = consistency_adjustment(scores)

    final_score = base_score + adjustment

    final_score = max(min(final_score, 100), 0)

    return round(final_score, 2)


# ---------------------------------
# Example
# ---------------------------------

if __name__ == "__main__":

    scores = {
        "ats": 90,
        "technical": 40,
        "hr": 85
    }

    print("Adjustment :", consistency_adjustment(scores))
    print("Final Score:", refined_final_score(scores, 75))