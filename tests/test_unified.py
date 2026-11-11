def test_unified():

    from ai_core.unified_scoring_engine import (

        calculate_unified_score
    )

    result = calculate_unified_score(

        80,

        70,

        85,

        {

            "ats": 0.3,

            "screening": 0.3,

            "hr": 0.4
        }
    )

    assert result > 0

    print("Test Passed")