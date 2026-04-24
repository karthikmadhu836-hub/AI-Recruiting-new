import re
from datetime import datetime
from utils.logger import get_logger

logger = get_logger()

# -------- Normalize Text --------
def normalize_text(text):
    return text.lower()

# -------- Extract Experience Blocks --------
def extract_experience_blocks(text):
    lines = text.split("\n")
    exp_lines = []

    for line in lines:
        if "company" in line or "worked" in line or "experience" in line:
            exp_lines.append(line)

    return exp_lines

# -------- Extract Duration --------
def extract_duration(text):
    matches = re.findall(r'(\d{4})\s*-\s*(\d{4}|present)', text)
    durations = []

    for start, end in matches:
        start_year = int(start)
        end_year = datetime.now().year if end == "present" else int(end)

        durations.append(end_year - start_year)

    return durations

# -------- Total Experience --------
def calculate_total_experience(durations):
    return sum(durations)

# -------- Extract Roles --------
def extract_roles(text):
    roles = []
    keywords = ["developer", "engineer", "analyst", "intern"]

    for word in keywords:
        if word in text:
            roles.append(word)

    return list(set(roles))

# -------- Extract Companies --------
def extract_companies(text):
    companies = []
    # simple heuristic: words after "at"
    matches = re.findall(r'at\s+([a-zA-Z0-9 ]+)', text)

    for m in matches:
        companies.append(m.strip())

    return list(set(companies))

# -------- MAIN FUNCTION --------
def parse_experience(text):
    text = normalize_text(text)

    durations = extract_duration(text)

    experience_data = {
        "companies": extract_companies(text),
        "roles": extract_roles(text),
        "total_experience_years": calculate_total_experience(durations),
        "durations": durations
    }

    logger.info("Experience parsed successfully")
    return experience_data