def test_stability():

    from interview_ai.stable_hr_ai import (

        stable_hr_evaluation
    )

    result = stable_hr_evaluation(

        [50, 60, 90, 30]
    )

    assert (

        result["stable_score"]

        > 0
    )

    print("Test Passed")


if __name__ == "__main__":

    test_stability()