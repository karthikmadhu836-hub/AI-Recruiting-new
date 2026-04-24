import re
from utils.logger import get_logger

logger = get_logger()

# -------- Section Keywords --------
SECTION_KEYWORDS = {
    "skills": ["skills", "technical skills", "key skills"],
    "experience": ["experience", "work experience", "employment"],
    "education": ["education", "academic"],
    "certifications": ["certifications", "certificates"],
    "projects": ["projects", "project work"]
}

# -------- Normalize Text --------
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'\n+', '\n', text)
    return text

# -------- Detect Sections --------
def classify_sections(text):
    text = normalize_text(text)
    lines = text.split("\n")

    sections = {
        "skills": "",
        "experience": "",
        "education": "",
        "certifications": "",
        "projects": ""
    }

    current_section = None

    for line in lines:
        line = line.strip()

        # Detect section heading
        for section, keywords in SECTION_KEYWORDS.items():
            if any(keyword in line for keyword in keywords):
                current_section = section
                break

        # Add content to section
        if current_section:
            sections[current_section] += line + " "

    logger.info("Sections classified successfully")
    return sections