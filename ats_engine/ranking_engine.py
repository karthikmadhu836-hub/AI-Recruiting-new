# -------------------------------
# Sort Candidates by Score
# -------------------------------
def rank_candidates(candidates):
    """
    Sort candidates in descending order of final_score
    """
    ranked = sorted(
        candidates,
        key=lambda x: x.get("final_score", 0),
        reverse=True
    )

    # Assign rank
    for idx, candidate in enumerate(ranked, start=1):
        candidate["rank"] = idx

    return ranked


# -------------------------------
# Threshold Configuration
# -------------------------------
THRESHOLDS = {
    "shortlist": 75,
    "review": 50
}


# -------------------------------
# Candidate Classification
# -------------------------------
def classify_candidate(score):
    if score >= THRESHOLDS["shortlist"]:
        return "Shortlisted"
    elif score >= THRESHOLDS["review"]:
        return "Review"
    else:
        return "Rejected"


# -------------------------------
# Apply Shortlisting Logic
# -------------------------------
def apply_shortlisting(candidates):
    for candidate in candidates:
        score = candidate.get("final_score", 0)
        candidate["status"] = classify_candidate(score)

    return candidates


# -------------------------------
# Top Candidate Selector
# -------------------------------
def get_top_candidates(candidates, top_n=5):
    return candidates[:top_n]


# -------------------------------
# Summary Generator (NEW)
# -------------------------------
def generate_summary(candidates):
    summary = {
        "total_candidates": len(candidates),
        "shortlisted": 0,
        "review": 0,
        "rejected": 0
    }

    for c in candidates:
        status = c.get("status")
        if status == "Shortlisted":
            summary["shortlisted"] += 1
        elif status == "Review":
            summary["review"] += 1
        elif status == "Rejected":
            summary["rejected"] += 1

    return summary


# -------------------------------
# Complete Ranking Pipeline
# -------------------------------
def ranking_pipeline(candidates, job_id=None):
    ranked = rank_candidates(candidates)
    shortlisted = apply_shortlisting(ranked)
    top_candidates = get_top_candidates(shortlisted)

    return {
        "job_id": job_id,
        "summary": generate_summary(shortlisted),
        "ranked_list": shortlisted,
        "top_candidates": top_candidates
    }