import re
from utils.logger import get_logger

logger = get_logger()

# -------- Normalize Text --------
def normalize_text(text):
    return text.lower()

# -------- Extract Degree --------
def extract_degree(text):
    degrees = ["btech", "mtech", "bsc", "msc", "bachelor", "master"]
    found = []

    for deg in degrees:
        if deg in text:
            found.append(deg)

    return list(set(found))

# -------- Extract Field --------
def extract_field(text):
    fields = ["computer science", "information technology", "data science", "electronics", "mechanical"]
    
    for field in fields:
        if field in text:
            return field

    return "not specified"

# -------- Extract Institution --------
def extract_institution(text):
    matches = re.findall(r'(college|university|institute)\s+[a-zA-Z ]+', text)
    return list(set(matches))

# -------- Extract Graduation Year --------
def extract_year(text):
    years = re.findall(r'(20\d{2})', text)
    return list(set(years))

# -------- Extract Certifications --------
def extract_certifications(text):
    cert_keywords = ["certified", "certification", "aws", "google", "azure"]
    certs = []

    for word in cert_keywords:
        if word in text:
            certs.append(word)

    return list(set(certs))

# -------- MAIN FUNCTION --------
def parse_education(text):
    text = normalize_text(text)

    education_data = {
        "degree": extract_degree(text),
        "field": extract_field(text),
        "institution": extract_institution(text),
        "graduation_year": extract_year(text),
        "certifications": extract_certifications(text)
    }

    logger.info("Education data extracted successfully")
    return education_data