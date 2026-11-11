def generate_hiring_report(
    candidate_id,
    ats,
    screening,
    hr,
    technical,
    machine_test,
    behavior,
    decision,
):
    """
    Generate a recruiter-friendly hiring report.
    """

    strengths = []
    weaknesses = []
    risks = []

    # ATS
    if ats >= 75:
        strengths.append("Strong resume-job match")
    else:
        weaknesses.append("Weak resume alignment")

    # Screening
    if screening >= 70:
        strengths.append("Good screening performance")
    else:
        weaknesses.append("Screening responses need improvement")

    # HR
    if hr >= 75:
        strengths.append("Strong HR interview performance")
    else:
        weaknesses.append("HR responses lacked depth")

    # Technical
    if technical >= 80:
        strengths.append("Excellent technical skills")
    else:
        weaknesses.append("Technical depth needs improvement")

    # Machine Test
    if machine_test >= 75:
        strengths.append("Good practical coding ability")
    else:
        weaknesses.append("Weak real-world execution")

    # Behavior
    if behavior.get("risk_level") != "Low Risk":
        risks.append("Behavioral concerns detected")

    if behavior.get("integrity") != "Low Risk":
        risks.append("Integrity risk detected")

    return {
        "candidate_id": candidate_id,
        "scores": {
            "ats": ats,
            "screening": screening,
            "hr": hr,
            "technical": technical,
            "machine_test": machine_test,
        },
        "behavior": behavior,
        "summary": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risks": risks,
        },
        "final_recommendation": decision,
    }


def hiring_report_pipeline(data):
    return generate_hiring_report(
        data["candidate_id"],
        data["ats"],
        data["screening"],
        data["hr"],
        data["technical"],
        data["machine_test"],
        data["behavior"],
        data["decision"],
    )


if __name__ == "__main__":

    sample = {
        "candidate_id": "C12001",
        "ats": 78,
        "screening": 72,
        "hr": 80,
        "technical": 85,
        "machine_test": 76,
        "behavior": {
            "confidence": 82,
            "risk_level": "Low Risk",
            "integrity": "Moderate Risk",
        },
        "decision": "Selected",
    }

    report = hiring_report_pipeline(sample)

    from pprint import pprint

    pprint(report)