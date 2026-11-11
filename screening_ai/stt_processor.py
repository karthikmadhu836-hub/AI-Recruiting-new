import re

# -------------------------------
# Simulated Speech-to-Text Engine
# -------------------------------
def speech_to_text(audio_input):
    """
    Simulated STT engine.
    Replace later with Whisper / Google STT.
    """

    return {
        "text": str(audio_input),
        "confidence": 0.92
    }


# -------------------------------
# Filler Words
# -------------------------------
FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "hmm"
]


# -------------------------------
# Remove Fillers
# -------------------------------
def remove_fillers(text):

    for word in FILLER_WORDS:
        pattern = rf"\b{re.escape(word)}\b"

        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE
        )

    return text


# -------------------------------
# Fix Punctuation
# -------------------------------
def fix_punctuation(text):

    text = text.strip()

    if not text:
        return text

    # Capitalize first character
    text = text[0].upper() + text[1:]

    # Add punctuation if missing
    if not text.endswith((".", "!", "?")):
        text += "."

    return text


# -------------------------------
# Normalize Text
# -------------------------------
def normalize_text(text):

    text = text.lower()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -------------------------------
# Handle Interrupted Speech
# -------------------------------
def handle_interruptions(text):

    # Remove repeated characters
    text = re.sub(r"(.)\1{2,}", r"\1", text)

    return text


# -------------------------------
# Silence Detection
# -------------------------------
def detect_silence(text):

    if not text:
        return True

    if len(text.strip()) < 2:
        return True

    return False


# -------------------------------
# Main Cleaning Pipeline
# -------------------------------
def clean_transcript(audio_input):

    stt_result = speech_to_text(audio_input)

    raw_text = stt_result.get("text", "")
    confidence = stt_result.get("confidence", 0.0)

    # Silence detection
    if detect_silence(raw_text):

        return {
            "clean_text": "",
            "confidence": confidence,
            "status": "silence_detected"
        }

    # Cleaning steps
    text = remove_fillers(raw_text)

    text = handle_interruptions(text)

    text = normalize_text(text)

    text = fix_punctuation(text)

    return {
        "clean_text": text,
        "confidence": confidence,
        "status": "processed"
    }