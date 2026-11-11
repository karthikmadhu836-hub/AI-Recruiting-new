import re

# -------------------------------
# Intent Keyword Mapping
# -------------------------------
INTENT_MAP = {
    "introduction": [
        "introduce",
        "about myself",
        "background"
    ],

    "experience": [
        "experience",
        "years",
        "worked",
        "role"
    ],

    "skills": [
        "skills",
        "technologies",
        "tools"
    ],

    "salary": [
        "salary",
        "ctc",
        "pay",
        "lpa"
    ],

    "availability": [
        "notice period",
        "available",
        "join",
        "immediate"
    ]
}


# -------------------------------
# Skill Database
# -------------------------------
SKILL_DB = [
    "python",
    "java",
    "django",
    "react",
    "sql",
    "flask",
    "node",
    "docker"
]


# -------------------------------
# Intent Classification
# -------------------------------
def classify_intent(text):

    text_lower = text.lower()

    for intent, keywords in INTENT_MAP.items():

        for keyword in keywords:

            if keyword in text_lower:
                return intent

    return "unknown"


# -------------------------------
# Skill Extraction
# -------------------------------
def extract_skills(text):

    text_lower = text.lower()

    found_skills = []

    for skill in SKILL_DB:

        if skill in text_lower:
            found_skills.append(skill)

    return found_skills


# -------------------------------
# Experience Extraction
# -------------------------------
def extract_experience(text):

    match = re.search(
        r"(\d+)\s*(years|year)",
        text.lower()
    )

    if match:
        return int(match.group(1))

    return 0


# -------------------------------
# Salary Extraction
# -------------------------------
def extract_salary(text):

    match = re.search(
        r"(\d+)\s*(lpa|lakhs|k)",
        text.lower()
    )

    if match:
        return match.group(0)

    return None


# -------------------------------
# Availability Extraction
# -------------------------------
def extract_availability(text):

    text_lower = text.lower()

    if "immediate" in text_lower:
        return "Immediate"

    elif "notice" in text_lower:
        return "Notice Period"

    return "Unknown"


# -------------------------------
# Off-topic Detection
# -------------------------------
def is_off_topic(intent):

    return intent == "unknown"


# -------------------------------
# Vague Answer Detection
# -------------------------------
def is_vague(text):

    vague_words = [
        "maybe",
        "not sure",
        "don't know",
        "can’t say"
    ]

    text_lower = text.lower()

    return any(word in text_lower for word in vague_words)


# -------------------------------
# Missing Answer Detection
# -------------------------------
def detect_missing_answer(text):

    if not text:
        return True

    if len(text.strip()) < 3:
        return True

    return False


# -------------------------------
# Main Processing Function
# -------------------------------
def process_answer(question_id, answer_text):

    missing = detect_missing_answer(answer_text)

    intent = classify_intent(answer_text)

    structured = {
        "question_id": question_id,

        "original_text": answer_text,

        "intent": intent,

        "skills": extract_skills(answer_text),

        "experience_years": extract_experience(answer_text),

        "salary": extract_salary(answer_text),

        "availability": extract_availability(answer_text),

        "off_topic": is_off_topic(intent),

        "is_vague": is_vague(answer_text),

        "missing_answer": missing
    }

    return structured


# -------------------------------
# Batch Processing
# -------------------------------
def process_answers_batch(answers):

    results = []

    for ans in answers:

        result = process_answer(
            ans["question_id"],
            ans["text"]
        )

        results.append(result)

    return results