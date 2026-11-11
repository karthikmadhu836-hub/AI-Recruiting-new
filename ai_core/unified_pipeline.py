"""
Unified Candidate Scoring Pipeline
Zecpath AI
"""

from unified_scoring_engine import (

    calculate_unified_score,

    get_weights
)

from hiring_fit import (

    calculate_hiring_fit
)


def unified_scoring_pipeline(

    candidate_id,

    ats,

    screening,

    hr,

    candidate_type="fresher"
):

    weights = get_weights(

        candidate_type
    )

    final_score = calculate_unified_score(

        ats_score=ats,

        screening_score=screening,

        hr_score=hr,

        weights=weights
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

        "candidate_id":

            candidate_id,

        "scores": {

            "ats": ats,

            "screening": screening,

            "hr": hr
        },

        "weights":

            weights,

        "final_score":

            final_score,

        "decision":

            decision,

        "hiring_fit": {

            "percentage":

                fit[
                    "hiring_fit_percentage"
                ],

            "category":

                fit[
                    "fit_category"
                ]
        },

        "explanation": {

            "ats":

                "Strong resume match and skill alignment",

            "screening":

                "Good response quality but minor gaps",

            "hr":

                "Strong communication and confidence"
        }
    }


# -------------------------------
# SAMPLE EXECUTION
# -------------------------------
if __name__ == "__main__":

    result = unified_scoring_pipeline(

        candidate_id="C500",

        ats=78,

        screening=72,

        hr=85,

        candidate_type="fresher"
    )

    print(result)