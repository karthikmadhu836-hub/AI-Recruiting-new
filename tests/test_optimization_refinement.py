from ai_core.optimized_ai_engine import adjust_decision
from ai_core.refined_scoring_logic import refined_final_score
from nlp.intent_refinement import refined_intent_detection


def test_adjust_decision():
    decision = adjust_decision(85, 90, "High Risk")
    assert decision == "Hold / Review"


def test_refined_score():
    scores = {
        "ats": 90,
        "technical": 85,
        "hr": 88,
        "screening": 87
    }

    final = refined_final_score(scores, 87)
    assert final > 0


def test_intent_detection():
    intent = refined_intent_detection(
        "I developed a machine learning project using Python."
    )
    assert intent == "experience"


if __name__ == "__main__":
    test_adjust_decision()
    test_refined_score()
    test_intent_detection()
    print("✅ Day 54 Optimization & Refinement tests passed.")