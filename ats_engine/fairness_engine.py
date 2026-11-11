import re

# -------------------------------
# Score Normalization (0–100 scaling)
# -------------------------------
def normalize_scores(candidate_scores):
    """
    Apply min-max normalization across candidates
    """
    if not candidate_scores:
        return candidate_scores

    scores = [c.get("final_score", 0) for c in candidate_scores]

    min_score = min(scores)
    max_score = max(scores)

    # Avoid division by zero
    if max_score == min_score:
        for c in candidate_scores:
            c["normalized_score"] = c.get("final_score", 0)
        return candidate_scores

    for c in candidate_scores:
        c["normalized_score"] = round(
            ((c.get("final_score", 0) - min_score) / (max_score - min_score)) * 100,
            2
        )

    return candidate_scores


# -------------------------------
# Bias Reduction (Mask Sensitive Fields)
# -------------------------------
def mask_sensitive_data(candidate):
    """
    Mask personal attributes
    """
    sensitive_fields = ["name", "gender", "age", "photo", "location"]

    masked_profile = {}

    for field in sensitive_fields:
        if field in candidate:
            masked_profile[field] = "MASKED"

    candidate["masked_profile"] = masked_profile

    return candidate


# -------------------------------
# Keyword Bias Reduction
# -------------------------------
def reduce_keyword_bias(skill_score, semantic_score):
    """
    Reduce over-dependence on keyword matching
    """
    adjusted_score = (0.6 * semantic_score) + (0.4 * skill_score)
    return round(adjusted_score, 2)


# -------------------------------
# Fair Score Generator
# -------------------------------
def generate_fair_score(candidate):
    """
    Generate bias-reduced score
    """
    skill_score = candidate.get("skill_score", 0)
    semantic_score = candidate.get("semantic_score", 0)

    fair_score = reduce_keyword_bias(skill_score, semantic_score)

    candidate["fair_score"] = fair_score

    return candidate