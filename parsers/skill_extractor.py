import re
from collections import defaultdict
from utils.logger import get_logger

logger = get_logger()

# -------- Master Skill Dictionary --------
SKILL_DB = {
    "python": ["python", "python3"],
    "java": ["java"],
    "sql": ["sql", "mysql", "postgres"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics"],
    "excel": ["excel"],
    "power bi": ["power bi"],
    "communication": ["communication"],
    "leadership": ["leadership"],
    "mern": ["mern", "mongodb express react node"],
    "mean": ["mean", "mongodb express angular node"]
}

# -------- Normalize Text --------
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return text

# -------- Extract Skills --------
def extract_skills(text):
    text = normalize_text(text)
    skill_scores = defaultdict(int)

    for skill, variations in SKILL_DB.items():
        for var in variations:
            if var in text:
                skill_scores[skill] += 1

    # Deduplicate + normalize
    extracted = list(skill_scores.keys())

    # Confidence scoring
    skill_confidence = {
        skill: min(1.0, score / 3)  # normalize score
        for skill, score in skill_scores.items()
    }

    logger.info("Skills extracted successfully")

    return extracted, skill_confidence