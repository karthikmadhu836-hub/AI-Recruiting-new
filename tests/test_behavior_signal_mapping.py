from behavior_ai.signal_mapping import (
    calculate_behavior_score,
    generate_behavior_report
)


def test_behavior_signal_mapping():

    signals = {

        "eye_focus": 0.7,

        "head_stability": 0.7,

        "engagement": 0.7,

        "distraction": 0.3

    }

    score = calculate_behavior_score(signals)

    report = generate_behavior_report(signals)

    assert score > 0
    assert "behavior_score" in report

    print("✅ Behavior Signal Mapping Test Passed")
    print(report)


if __name__ == "__main__":
    test_behavior_signal_mapping()