from interview_ai.final_hr_module import run_hr_interview


def test_final_system():

    result = run_hr_interview(
        candidate_id="C1",
        answers=[],
        communication={
            "communication_score": 70
        },
        behavior={
            "confidence": {
                "confidence_score": 70
            },
            "behavioral_score": 70,
            "contradiction": False
        }
    )

    assert "final_score" in result
    assert "decision" in result

    print("✅ Final HR Module Test Passed")


if __name__ == "__main__":
    test_final_system()