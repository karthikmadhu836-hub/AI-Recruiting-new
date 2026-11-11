"""
AI Interview Summary Generator
Zecpath AI
"""

# --------------------------------------------------
# Natural Language Summary Generator
# --------------------------------------------------
def generate_natural_summary(
    strengths,
    weaknesses,
    risks,
    culture_fit,
    decision
):
    return f"""
The candidate demonstrates {', '.join(strengths[:2]) if strengths else 'some strengths'}.
However, there are concerns such as {', '.join(weaknesses[:2]) if weaknesses else 'minor weaknesses'}.
Risk factors include {', '.join(risks) if risks else 'no major risks'}.
Cultural fit is assessed as {culture_fit}.
Final Recommendation: {decision}.
""".strip()


# --------------------------------------------------
# Main Interview Summary Generator
# --------------------------------------------------
def generate_interview_summary(
    candidate_id,
    hr_scores,
    communication,
    behavior,
    answers
):
    strengths = []
    weaknesses = []
    risks = []
    inconsistencies = []

    # ----------------------------------------------
    # HR Score Analysis
    # ----------------------------------------------
    for item in hr_scores:
        if item.get("final_score", 0) >= 80:
            strengths.append(
                f"Strong performance in {item.get('question_id', 'Unknown')}"
            )

        elif item.get("final_score", 0) < 50:
            weaknesses.append(
                f"Weak response in {item.get('question_id', 'Unknown')}"
            )

    # ----------------------------------------------
    # Communication Analysis
    # ----------------------------------------------
    communication_score = communication.get(
        "communication_score",
        0
    )

    if communication_score >= 80:
        strengths.append("Excellent communication skills")

    elif communication_score < 50:
        weaknesses.append("Poor communication clarity")

    # ----------------------------------------------
    # Behavior Analysis
    # ----------------------------------------------
    confidence_score = (
        behavior.get("confidence", {})
        .get("confidence_score", 0)
    )

    if confidence_score < 60:
        risks.append("Low confidence detected")

    if behavior.get("contradiction", False):
        inconsistencies.append(
            "Contradictory statements observed"
        )

    # ----------------------------------------------
    # Cultural Fit Detection
    # ----------------------------------------------
    culture_fit = "Good"

    answer_text = " ".join(
        str(a) for a in answers
    ).lower()

    if "team" in answer_text:
        strengths.append("Shows teamwork orientation")
    else:
        culture_fit = "Moderate"

    # ----------------------------------------------
    # HR Average Score
    # ----------------------------------------------
    if hr_scores:
        avg_hr_score = (
            sum(
                item.get("final_score", 0)
                for item in hr_scores
            )
            / len(hr_scores)
        )
    else:
        avg_hr_score = 0

    # ----------------------------------------------
    # Overall Score Calculation
    # ----------------------------------------------
    overall_score = (
        communication_score * 0.30
        + behavior.get("behavioral_score", 0) * 0.30
        + avg_hr_score * 0.40
    )

    # ----------------------------------------------
    # Final Hiring Decision
    # ----------------------------------------------
    if overall_score >= 60:
        decision = "Strong Hire"

    elif overall_score >= 35:
        decision = "Consider"

    else:
        decision = "Reject"

    # ----------------------------------------------
    # Return Final Report
    # ----------------------------------------------
    return {
        "candidate_id": candidate_id,
        "overall_score": round(overall_score, 2),
        "decision": decision,
        "summary": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risks": risks,
            "inconsistencies": inconsistencies,
            "cultural_fit": culture_fit
        },
        "natural_language_summary": generate_natural_summary(
            strengths,
            weaknesses,
            risks,
            culture_fit,
            decision
        )
    }