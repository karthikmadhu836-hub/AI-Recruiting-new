from integrity_ai.detection_logic import (
    calculate_integrity_score,
    evaluate_integrity
)


def test_integrity_detection():

    events = {

        "tab_switch": 2,

        "focus_loss": 1,

        "voice_detect": 0,

        "gaze_off": 2

    }

    score = calculate_integrity_score(events)

    report = evaluate_integrity(events)

    assert score > 0
    assert "risk_level" in report

    print("✅ Integrity Detection Test Passed")
    print(report)


if __name__ == "__main__":
    test_integrity_detection()