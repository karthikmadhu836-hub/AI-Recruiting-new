"""
Recommendation Logic Pipeline
Zecpath AI
"""

from ai_core.decision_engine import (

    generate_decision,

    calculate_decision_confidence,

    generate_explanation

)


def recommendation_pipeline(

    candidate_id,

    scores,

    behavior_risk,

    integrity_risk

):

    final_score = scores.get("final_score", 0)

    decision, adjusted_score = generate_decision(

        final_score,

        behavior_risk,

        integrity_risk

    )

    confidence = calculate_decision_confidence(

        list(scores.values())

    )

    explanation = generate_explanation(

        scores,

        decision

    )

    return {

        "candidate_id": candidate_id,

        "final_score": final_score,

        "adjusted_score": adjusted_score,

        "decision": decision,

        "confidence_score": confidence,

        "risks": {

            "behavior": behavior_risk,

            "integrity": integrity_risk

        },

        "explanation": explanation

    }


if __name__ == "__main__":

    sample_scores = {

        "technical": 85,

        "communication": 82,

        "behavior": 85,

        "integrity": 90,

        "final_score": 84

    }

    result = recommendation_pipeline(

        "C10001",

        sample_scores,

        "Low Risk",

        "Moderate Risk"

    )

    print(result)