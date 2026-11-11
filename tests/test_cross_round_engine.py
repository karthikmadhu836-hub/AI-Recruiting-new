from ai_core.cross_round_engine import (
    calculate_final_score,
    aggregation_pipeline
)


def test_cross_round_engine():

    scores = {

        "ats": 70,

        "screening": 70,

        "hr": 70,

        "technical": 70,

        "machine_test": 70

    }

    weights = {

        "ats": 0.20,

        "screening": 0.20,

        "hr": 0.20,

        "technical": 0.20,

        "machine_test": 0.20

    }

    score = calculate_final_score(
        scores,
        weights
    )

    assert score == 70.0

    result = aggregation_pipeline(
        "C001",
        scores,
        "technical"
    )

    print("✅ Cross-Round Aggregation Test Passed")
    print(result)


if __name__ == "__main__":
    test_cross_round_engine()