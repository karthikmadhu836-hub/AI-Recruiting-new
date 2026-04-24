import re


# -------------------------------
# 1. TEXT NORMALIZATION
# -------------------------------
def normalize_text(text):
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# -------------------------------
# 2. MASK PERSONAL INFORMATION
# -------------------------------
def mask_personal_info(text):

    # Emails
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)

    # Phone numbers
    text = re.sub(r'\b\d{10}\b', '[PHONE]', text)

    # Names (simple heuristic)
    text = re.sub(r'\b(name|mr|ms|mrs)\b.*', '[NAME]', text)

    return text


# -------------------------------
# 3. SCORE NORMALIZATION
# -------------------------------
def normalize_score(score):
    """
    Ensure score is between 0 and 1
    """
    return max(0, min(score, 1))


# -------------------------------
# 4. REDUCE KEYWORD BIAS
# -------------------------------
def reduce_keyword_bias(skill_score, semantic_score):
    """
    Balance keyword vs semantic importance
    """
    # Give more importance to semantic meaning
    return (skill_score * 0.4) + (semantic_score * 0.6)


# -------------------------------
# 5. BIAS CHECK (BASIC)
# -------------------------------
def detect_bias_indicators(text):

    bias_keywords = [
        "male", "female", "age", "young", "old",
        "married", "single", "religion", "caste"
    ]

    found = [word for word in bias_keywords if word in text]

    return found