"""
Cross-Round Aggregation Engine
Zecpath AI
"""

# ----------------------------------------
# Default Weights
# ----------------------------------------

DEFAULT_WEIGHTS = {

    "ats": 0.20,

    "screening": 0.15,

    "hr": 0.20,

    "technical": 0.25,

    "machine_test": 0.20

}


# ----------------------------------------
# Role-Based Weights
# ----------------------------------------

ROLE_WEIGHTS = {

    "fresher": {

        "ats": 0.20,

        "screening": 0.20,

        "hr": 0.25,

        "technical": 0.20,

        "machine_test": 0.15

    },

    "experienced": {

        "ats": 0.25,

        "screening": 0.10,

        "hr": 0.20,

        "technical": 0.25,

        "machine_test": 0.20

    },

    "technical": {

        "ats": 0.15,

        "screening": 0.10,

        "hr": 0.15,

        "technical": 0.35,

        "machine_test": 0.25

    },

    "non_technical": {

        "ats": 0.25,

        "screening": 0.20,

        "hr": 0.35,

        "technical": 0.10,

        "machine_test": 0.10

    }

}


# ----------------------------------------
# Select Weights
# ----------------------------------------

def get_weights(role_type=None):

    return ROLE_WEIGHTS.get(
        role_type,
        DEFAULT_WEIGHTS
    )


# ----------------------------------------
# Normalize Scores
# ----------------------------------------

def normalize_scores(scores):

    normalized = {}

    for key, value in scores.items():

        normalized[key] = max(
            min(value, 100),
            0
        )

    return normalized


# ----------------------------------------
# Final Score Calculation
# ----------------------------------------

def calculate_final_score(
    scores,
    weights
):

    final = 0

    for stage in weights:

        final += (

            scores.get(stage, 0)

            *

            weights[stage]

        )

    return round(final, 2)


# ----------------------------------------
# Aggregation Pipeline
# ----------------------------------------

from ai_core.hiring_fit_calculator import (
    calculate_hiring_fit
)


def aggregation_pipeline(

    candidate_id,

    scores,

    role_type="technical"

):

    scores = normalize_scores(
        scores
    )

    weights = get_weights(
        role_type
    )

    final_score = calculate_final_score(

        scores,

        weights

    )

    fit = calculate_hiring_fit(
        final_score
    )

    if final_score >= 75:

        decision = "Hire"

    elif final_score >= 55:

        decision = "Consider"

    else:

        decision = "Reject"

    return {

        "candidate_id": candidate_id,

        "scores": scores,

        "weights": weights,

        "final_score": final_score,

        "decision": decision,

        "hiring_fit": fit

    }


# ----------------------------------------
# Example
# ----------------------------------------

if __name__ == "__main__":

    sample_scores = {

        "ats": 75,

        "screening": 70,

        "hr": 82,

        "technical": 88,

        "machine_test": 80

    }

    result = aggregation_pipeline(

        "C9001",

        sample_scores,

        "technical"

    )

    print(result)