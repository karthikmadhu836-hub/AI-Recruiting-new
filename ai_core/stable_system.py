"""
Zecpath AI
Day 57 - Stable AI System
"""


# ---------------------------------
# Safe Score Normalization
# ---------------------------------

def safe_score(value):

    try:
        value = float(value)
    except (ValueError, TypeError):
        return 0

    return max(min(value, 100), 0)


# ---------------------------------
# Stable Aggregation
# ---------------------------------

def stable_aggregate(scores):

    cleaned = {
        key: safe_score(value)
        for key, value in scores.items()
    }

    if not cleaned:
        return 0

    average = sum(cleaned.values()) / len(cleaned)

    return round(average, 2)


# ---------------------------------
# Stable Decision Logic
# ---------------------------------

def stable_decision(score):

    if score >= 75:
        return "Selected"

    if score >= 55:
        return "Hold / Review"

    return "Rejected"


# ---------------------------------
# Final Stable Pipeline
# ---------------------------------

def stable_pipeline(candidate_id, scores):

    final_score = stable_aggregate(scores)

    decision = stable_decision(final_score)

    return {
        "candidate_id": candidate_id,
        "final_score": final_score,
        "decision": decision,
        "status": "stable"
    }


# ---------------------------------
# Example Execution
# ---------------------------------

if __name__ == "__main__":

    sample_scores = {
        "ats": 85,
        "screening": 78,
        "hr": 80,
        "technical": 88,
        "machine_test": 82
    }

    print(stable_pipeline("C1001", sample_scores))