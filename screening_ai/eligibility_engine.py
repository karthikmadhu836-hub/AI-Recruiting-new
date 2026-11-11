import logging

# ----------------------------------------
# LOGGER CONFIG
# ----------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EligibilityEngine")

# ----------------------------------------
# DEFAULT RULES
# ----------------------------------------
DEFAULT_RULES = {
    "min_ats_score": 40,
    "mandatory_skills": [],
    "min_experience": 0,
    "max_experience": 20,
    "allowed_locations": [],
    "availability_required": False
}


# ----------------------------------------
# SAFE VALUE
# ----------------------------------------
def safe_value(value, default):
    return value if value is not None else default


# ----------------------------------------
# SKILL MATCH %
# ----------------------------------------
def calculate_skill_match(candidate_skills, required_skills):

    if not required_skills:
        return 100

    candidate_skills = [
        str(skill).lower().strip()
        for skill in candidate_skills
    ]

    required_skills = [
        str(skill).lower().strip()
        for skill in required_skills
    ]

    matched = sum(
        1
        for skill in required_skills
        if skill in candidate_skills
    )

    return round(
        (matched / len(required_skills)) * 100,
        2
    )


# ----------------------------------------
# EXPERIENCE SCORE
# ----------------------------------------
def calculate_experience_score(
    candidate_exp,
    min_exp
):

    candidate_exp = safe_value(
        candidate_exp,
        0
    )

    if candidate_exp >= min_exp:
        return 100

    return round(
        (candidate_exp / max(min_exp, 1)) * 100,
        2
    )


# ----------------------------------------
# ELIGIBILITY ENGINE
# ----------------------------------------
def evaluate_candidate(
    candidate,
    rules=DEFAULT_RULES
):

    ats_score = safe_value(
        candidate.get("final_score"),
        0
    )

    skills = safe_value(
        candidate.get("skills"),
        []
    )

    experience = safe_value(
        candidate.get("total_experience"),
        0
    )

    skill_match = calculate_skill_match(
        skills,
        rules["mandatory_skills"]
    )

    exp_score = calculate_experience_score(
        experience,
        rules["min_experience"]
    )

    # ----------------------------------------
    # FINAL ELIGIBILITY SCORE
    # ----------------------------------------
    eligibility_score = (

        ats_score * 0.60 +

        skill_match * 0.25 +

        exp_score * 0.15

    )

    # ----------------------------------------
    # DECISION
    # ----------------------------------------
    if eligibility_score >= 70:

        status = "Eligible"

    elif eligibility_score >= 50:

        status = "Review"

    else:

        status = "Rejected"

    logger.info(
        f"{candidate.get('candidate_id')} "
        f"=> {status}"
    )

    return {

        "candidate_id":
            candidate.get("candidate_id"),

        "eligibility_status":
            status,

        "eligibility_score":
            round(
                eligibility_score,
                2
            ),

        "checks": {

            "ats_score":
                ats_score,

            "skill_match_percent":
                skill_match,

            "experience_score":
                exp_score
        },

        "rules_used":
            rules
    }


# ----------------------------------------
# BATCH MODE
# ----------------------------------------
def evaluate_candidates_batch(
    candidates,
    rules
):

    results = []

    for candidate in candidates:

        results.append(

            evaluate_candidate(
                candidate,
                rules
            )
        )

    return results


# ----------------------------------------
# TEST
# ----------------------------------------
if __name__ == "__main__":

    sample_candidate = {

        "candidate_id": "C101",

        "final_score": 45,

        "skills": [
            "python",
            "sql",
            "excel"
        ],

        "total_experience": 2
    }

    sample_rules = {

        "mandatory_skills": [
            "python",
            "sql",
            "excel",
            "power bi"
        ],

        "min_experience": 1
    }

    result = evaluate_candidate(
        sample_candidate,
        sample_rules
    )

    print(result)