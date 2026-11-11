"""
Zecpath AI
Day 65 - Final Production System
"""


# ---------------------------------
# Score Normalization
# ---------------------------------

def normalize_score(value):
    """
    Normalize scores between 0 and 100.
    """
    try:
        value = float(value)
    except (ValueError, TypeError):
        return 0.0

    return max(0.0, min(value, 100.0))


# ---------------------------------
# Score Consistency Smoothing
# ---------------------------------

def smooth_scores(scores):
    """
    Reduce score variance between modules.
    """

    values = [normalize_score(v) for v in scores.values()]

    if not values:
        return {}

    average = sum(values) / len(values)

    smoothed = {}

    for module, score in scores.items():
        score = normalize_score(score)
        smoothed[module] = round((score * 0.7) + (average * 0.3), 2)

    return smoothed


# ---------------------------------
# Final Decision
# ---------------------------------

def final_decision(score):

    if score >= 80:
        return "Selected"

    elif score >= 60:
        return "Hold / Review"

    return "Rejected"


# ---------------------------------
# Production Pipeline
# ---------------------------------

def production_pipeline(candidate_id, scores):

    scores = smooth_scores(scores)

    final_score = round(sum(scores.values()) / len(scores), 2)

    return {
        "candidate_id": candidate_id,
        "scores": scores,
        "final_score": final_score,
        "decision": final_decision(final_score),
        "status": "production_ready"
    }


# ---------------------------------
# Example
# ---------------------------------

if __name__ == "__main__":

    sample_scores = {
        "ats": 90,
        "screening": 78,
        "hr": 82,
        "technical": 87,
        "machine_test": 84
    }

    print(production_pipeline("C001", sample_scores))