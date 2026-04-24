def calculate_experience_score(candidate_roles, jd_role):
    score = 0

    for role in candidate_roles:
        if role in jd_role.lower():
            score += 1

    return min(1.0, score / len(candidate_roles)) if candidate_roles else 0