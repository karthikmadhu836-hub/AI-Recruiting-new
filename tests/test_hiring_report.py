from ai_core.hiring_report_generator import generate_hiring_report


def test_hiring_report():

    report = generate_hiring_report(
        "C1",
        70,
        70,
        70,
        70,
        70,
        {
            "risk_level": "Low Risk",
            "integrity": "Low Risk",
        },
        "Selected",
    )

    assert "candidate_id" in report
    assert report["candidate_id"] == "C1"
    assert "scores" in report
    assert "summary" in report
    assert "final_recommendation" in report


if __name__ == "__main__":
    test_hiring_report()
    print("✅ Hiring Report Generator Test Passed")