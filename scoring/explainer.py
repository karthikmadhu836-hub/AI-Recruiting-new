def generate_explanation(skill, exp, edu, semantic, final):
    return {
        "final_score": final,
        "breakdown": {
            "skills": skill,
            "experience": exp,
            "education": edu,
            "semantic": semantic
        },
        "remarks": "Candidate evaluated based on multiple weighted parameters"
    }