from interview_ai.aptitude_scoring import calculate_aptitude_score


def test_aptitude():

    result = calculate_aptitude_score(
        "First I analyze the problem then I create a solution"
    )

    assert result["aptitude_score"] > 0