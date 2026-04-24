import re
import os
from utils.logger import get_logger

logger = get_logger()

# ----------- Skill List (expand later) -----------
SKILLS_DB = [
    "python", "java", "sql", "machine learning", "data analysis",
    "excel", "power bi", "communication", "leadership"
]

# ----------- Normalize Text -----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[^a-zA-Z0-9\s\n]', '', text)
    return text

# ----------- Extract Skills -----------
def extract_skills(text):
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))

# ----------- Extract Experience -----------
def extract_experience(text):
    match = re.findall(r'(\d+)\+?\s*years', text)
    if match:
        return max([int(x) for x in match])
    return 0

# ----------- Extract Role -----------
def extract_role(text):
    lines = text.split("\n")
    for line in lines:
        if "engineer" in line or "analyst" in line or "developer" in line:
            return line.strip()
    return "Not Found"

# ----------- Extract Education -----------
def extract_education(text):
    if "b.tech" in text or "bachelor" in text:
        return "Bachelor"
    if "m.tech" in text or "master" in text:
        return "Master"
    return "Not Specified"

# ----------- Main Parser -----------
def parse_jd(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned = clean_text(raw_text)

        jd_data = {
            "job_title": extract_role(cleaned),
            "skills": extract_skills(cleaned),
            "experience_required": extract_experience(cleaned),
            "education": extract_education(cleaned)
        }

        logger.info(f"Parsed JD: {file_path}")
        return jd_data

    except Exception as e:
        logger.error(f"Error parsing JD: {e}")
        return {}