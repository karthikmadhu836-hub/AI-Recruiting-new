def rank_candidates(results):
    return sorted(results, key=lambda x: x["score"], reverse=True)


def shortlist_candidates(results):
    """
    Dynamic threshold-based shortlisting
    Automatically adjusts based on score distribution
    """

    if not results:
        return [], [], []

    scores = [r["score"] for r in results]

    max_score = max(scores)
    min_score = min(scores)

    # --- Dynamic thresholds ---
    shortlist_threshold = max_score * 0.8
    reject_threshold = min_score + (max_score - min_score) * 0.2

    shortlisted = []
    rejected = []
    review = []

    for r in results:
        score = r["score"]

        if score >= shortlist_threshold:
            r["status"] = "shortlisted"
            shortlisted.append(r)

        elif score < reject_threshold:
            r["status"] = "rejected"
            rejected.append(r)

        else:
            r["status"] = "review"
            review.append(r)

    return shortlisted, review, rejected


def get_top_candidates(results, top_n=5):
    """
    Get Top N candidates per Job Description
    """

    jd_groups = {}

    # Group by JD
    for r in results:
        jd = r["jd"]
        jd_groups.setdefault(jd, []).append(r)

    top_candidates = {}

    for jd, candidates in jd_groups.items():
        sorted_candidates = sorted(
            candidates, key=lambda x: x["score"], reverse=True
        )
        top_candidates[jd] = sorted_candidates[:top_n]

    return top_candidates