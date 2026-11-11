from ai_core.decision_engine import generate_decision


def test_decision():

    decision, adjusted_score = generate_decision(

        85,

        "Low Risk",

        "Low Risk"

    )

    assert decision == "Selected"

    assert adjusted_score == 85

    print("✅ Decision Engine Test Passed")


if __name__ == "__main__":

    test_decision()