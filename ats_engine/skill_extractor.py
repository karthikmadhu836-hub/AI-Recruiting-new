import re

# ==========================================================
# MASTER SKILL DATABASE
# ==========================================================
SKILL_DB = {
    "python": ["python", "python3"],
    "java": ["java"],
    "c++": ["c++", "cpp"],
    "c": [" c "],
    "sql": ["sql", "mysql", "postgres", "postgresql"],
    "excel": ["excel", "microsoft excel"],
    "power bi": ["power bi"],
    "tableau": ["tableau"],

    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics"],
    "data science": ["data science"],

    "django": ["django"],
    "flask": ["flask"],
    "react": ["react", "reactjs"],
    "angular": ["angular"],
    "node": ["node", "nodejs"],
    "mongodb": ["mongodb"],

    "communication": [
        "communication",
        "communication skills"
    ],

    "leadership": [
        "leadership",
        "team leadership"
    ],

    "problem solving": [
        "problem solving",
        "problem-solving"
    ]
}

# ==========================================================
# STACKS
# ==========================================================
SKILL_STACKS = {
    "mern": [
        "mongodb",
        "express",
        "react",
        "node"
    ],

    "mean": [
        "mongodb",
        "express",
        "angular",
        "node"
    ]
}

# ==========================================================
# CLEAN TEXT
# ==========================================================
def clean_text(text):

    if not text:
        return ""

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s\+\#\.\-]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==========================================================
# EXTRACT SKILLS
# ==========================================================
def extract_skills(text):

    text = clean_text(text)

    found_skills = []

    for skill, variants in SKILL_DB.items():

        for variant in variants:

            pattern = r"\b" + re.escape(variant) + r"\b"

            if re.search(pattern, text):

                found_skills.append(skill)

                break

    # Detect MERN / MEAN
    for stack, stack_skills in SKILL_STACKS.items():

        if re.search(r"\b" + stack + r"\b", text):

            found_skills.extend(stack_skills)

    return sorted(list(set(found_skills)))


# ==========================================================
# CONFIDENCE SCORE
# ==========================================================
def calculate_confidence(skill, text):

    text = clean_text(text)

    count = len(
        re.findall(
            r"\b" + re.escape(skill) + r"\b",
            text
        )
    )

    if count >= 3:
        return 0.98

    elif count == 2:
        return 0.90

    elif count == 1:
        return 0.80

    return 0.50


# ==========================================================
# SKILLS WITH CONFIDENCE
# ==========================================================
def extract_skills_with_confidence(text):

    skills = extract_skills(text)

    results = []

    for skill in skills:

        results.append({

            "skill": skill,

            "confidence": round(
                calculate_confidence(skill, text),
                2
            )

        })

    return results


# ==========================================================
# PIPELINE COMPATIBILITY
# ==========================================================
def extract_skills_and_confidence(text):

    skills = extract_skills(text)

    confidence = {
        skill: calculate_confidence(skill, text)
        for skill in skills
    }

    return skills, confidence