"""
Integrity Detection Logic
Zecpath AI
"""

# ------------------------------------
# Threshold Configuration
# ------------------------------------
THRESHOLDS = {
    "tab_switch": 3,
    "focus_loss": 5,
    "voice_detect": 2,
    "gaze_off": 5
}


# ------------------------------------
# Malpractice Detection
# ------------------------------------
def detect_malpractice(events):

    flags = []

    if events.get("tab_switch", 0) > THRESHOLDS["tab_switch"]:
        flags.append("High Tab Switching")

    if events.get("focus_loss", 0) > THRESHOLDS["focus_loss"]:
        flags.append("Screen Focus Loss")

    if events.get("voice_detect", 0) > THRESHOLDS["voice_detect"]:
        flags.append("Multiple Voices Detected")

    if events.get("gaze_off", 0) > THRESHOLDS["gaze_off"]:
        flags.append("Frequent Gaze Deviation")

    return flags


# ------------------------------------
# Integrity Score
# ------------------------------------
def calculate_integrity_score(events):

    score = 100

    score -= events.get("tab_switch", 0) * 5
    score -= events.get("focus_loss", 0) * 3
    score -= events.get("voice_detect", 0) * 10
    score -= events.get("gaze_off", 0) * 4

    return max(score, 0)


# ------------------------------------
# Risk Level
# ------------------------------------
def risk_flagging(score):

    if score < 50:
        return "High Risk"

    elif score < 75:
        return "Moderate Risk"

    return "Low Risk"


# ------------------------------------
# Real-Time Warnings
# ------------------------------------
def generate_warning(events):

    warnings = []

    if events.get("tab_switch", 0) > 2:
        warnings.append(
            "Please stay on the interview screen."
        )

    if events.get("voice_detect", 0) > 1:
        warnings.append(
            "External voice detected. Please ensure you are alone."
        )

    if events.get("focus_loss", 0) > 3:
        warnings.append(
            "You seem distracted. Please focus on the interview."
        )

    return warnings


# ------------------------------------
# Behavioral + Integrity Score
# ------------------------------------
def combined_risk(
    behavior_score,
    integrity_score
):

    final = (
        behavior_score * 0.40 +
        integrity_score * 0.60
    )

    return round(final, 2)


# ------------------------------------
# Complete Evaluation
# ------------------------------------
def evaluate_integrity(events, behavior_score=80):

    integrity_score = calculate_integrity_score(events)

    return {

        "integrity_score": integrity_score,

        "risk_level": risk_flagging(
            integrity_score
        ),

        "flags": detect_malpractice(events),

        "warnings": generate_warning(events),

        "combined_score": combined_risk(
            behavior_score,
            integrity_score
        )

    }


# ------------------------------------
# Example
# ------------------------------------
if __name__ == "__main__":

    sample = {

        "tab_switch": 4,

        "focus_loss": 2,

        "voice_detect": 1,

        "gaze_off": 6

    }

    print(
        evaluate_integrity(sample)
    )