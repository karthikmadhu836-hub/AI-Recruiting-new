def calculate_final_score(skill_score, exp_score, edu_score, semantic_score, weights):
    final_score = (
        skill_score * weights["skills"] +
        exp_score * weights["experience"] +
        edu_score * weights["education"] +
        semantic_score * weights["semantic"]
    )
    return round(final_score, 2)