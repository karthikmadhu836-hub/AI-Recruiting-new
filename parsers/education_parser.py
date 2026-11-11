import re
from utils.logger import get_logger

logger = get_logger()

# -------------------------------
# Degree Mapping
# -------------------------------
DEGREE_MAP = {
    "btech": "B.Tech",
    "b.e": "B.Tech",
    "mtech": "M.Tech",
    "m.e": "M.Tech",
    "mba": "MBA",
    "bsc": "B.Sc",
    "msc": "M.Sc"
}

# -------------------------------
# Certification Categories
# -------------------------------
CERT_CATEGORIES = {
    "aws": "Cloud",
    "azure": "Cloud",
    "gcp": "Cloud",
    "python": "Programming",
    "data science": "Data",
    "machine learning": "AI",
    "scrum": "Management"
}

# -------------------------------
# Normalize Text (FIXED)
# -------------------------------
def clean_text(text):
    if isinstance(text, dict):
        text = text.get("cleaned_text", "")

    text = text.lower()

    # 🔥 normalize degrees like B.Tech → btech
    text = text.replace("b.tech", "btech")
    text = text.replace("m.tech", "mtech")
    text = text.replace("b.e", "be")
    text = text.replace("m.e", "me")

    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text

# -------------------------------
# Extract Education (NEW)
# -------------------------------
def extract_education(text):
    text = clean_text(text)
    education_list = []

    for key, value in DEGREE_MAP.items():
        if re.search(rf"\b{key}\b", text):
            year_match = re.findall(r"(20\d{2})", text)
            year = year_match[0] if year_match else None

            education_list.append({
                "degree": value,
                "field": "Not Specified",
                "institution": "Not Extracted",
                "year_of_completion": year
            })

    return education_list

# -------------------------------
# Extract Certifications (NEW)
# -------------------------------
def extract_certifications(text):
    text = clean_text(text)
    certifications = []

    for keyword, category in CERT_CATEGORIES.items():
        if keyword in text:
            certifications.append({
                "name": keyword.title(),
                "category": category
            })

    return certifications

# -------------------------------
# Education Relevance
# -------------------------------
def calculate_education_relevance(candidate_degree, required_degree):
    if not candidate_degree or not required_degree:
        return 0

    candidate_degree = candidate_degree.lower()
    required_degree = required_degree.lower()

    if candidate_degree == required_degree:
        return 1.0
    elif candidate_degree in ["m.tech", "mba"] and required_degree in ["b.tech", "b.e"]:
        return 0.8
    else:
        return 0.5

# -------------------------------
# Certification Relevance
# -------------------------------
def calculate_certification_relevance(certifications, job_skills):
    score = 0

    for cert in certifications:
        if cert["category"].lower() in [skill.lower() for skill in job_skills]:
            score += 1

    if len(certifications) == 0:
        return 0

    return round((score / len(certifications)) * 100, 2)

# -------------------------------
# OLD FUNCTION (FOR TESTS)
# -------------------------------
def parse_education(text):
    text = clean_text(text)

    education_data = {
        "education": extract_education(text),
        "certifications": extract_certifications(text)
    }

    logger.info("Education data extracted successfully")
    return education_data