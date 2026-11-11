import re

# -------------------------------
# Clean Background Noise
# -------------------------------
def clean_noise(text):

    # Remove noise markers
    text = re.sub(r"\[.*?\]", "", text)

    # Remove repeated characters
    text = re.sub(r"(.)\1{2,}", r"\1", text)

    return text.strip()


# -------------------------------
# Detect Language Mixing
# -------------------------------
def detect_language_mix(text):

    local_words = [
        "hai",
        "enna",
        "chetta",
        "bhai"
    ]

    for word in local_words:
        if word in text.lower():
            return True

    return False