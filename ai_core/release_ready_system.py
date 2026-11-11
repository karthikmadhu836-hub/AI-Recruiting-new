"""
Day 68 - Release Ready AI System
Zecpath AI Hiring Platform
"""

# -------------------------------
# Safe Value Handler
# -------------------------------

def safe_value(value, default=0):
    """
    Converts any score into a valid number
    between 0 and 100.
    """
    try:
        value = float(value)
    except (TypeError, ValueError):
        return default

    return max(0.0, min(value, 100.0))


# -------------------------------
# Score Validation
# -------------------------------

def validate_scores(scores):
    """
    Validate all module scores.
    """
    return {
        module: safe_value(score)
        for module, score in scores.items()
    }


# -------------------------------
# Final Score Aggregation
# -------------------------------

def final_aggregate(scores):
    scores = validate_scores(scores)

    if not scores:
        return 0.0

    return round(sum(scores.values()) / len(scores), 2)


# -------------------------------
# Decision Logic
# -------------------------------

def final_decision(score):

    if score >= 80:
        return "Selected"

    elif score >= 60:
        return "Hold / Review"

    return "Rejected"


# -------------------------------
# Release Pipeline
# -------------------------------

def release_pipeline(candidate_id, scores):

    validated_scores = validate_scores(scores)

    final_score = final_aggregate(validated_scores)

    decision = final_decision(final_score)

    return {
        "candidate_id": candidate_id,
        "scores": validated_scores,
        "final_score": final_score,
        "decision": decision,
        "status": "release_ready"
    }


# -------------------------------
# Demo
# -------------------------------

if __name__ == "__main__":

    sample_scores = {
        "ats": 120,
        "screening": 75,
        "hr": -5,
        "technical": 88
    }

    result = release_pipeline("C30001", sample_scores)

    print(result)