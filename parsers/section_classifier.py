import re

# -------------------------------------------------
# SECTION HEADINGS
# -------------------------------------------------
SECTION_KEYWORDS = {

    "summary": [
        "summary",
        "professional summary",
        "profile",
        "career objective",
        "objective"
    ],

    "skills": [
        "skills",
        "technical skills",
        "skill set",
        "core competencies"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history"
    ],

    "projects": [
        "projects",
        "project experience",
        "academic projects"
    ],

    "education": [
        "education",
        "academic background",
        "qualification",
        "qualifications"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses"
    ]
}


# -------------------------------------------------
# NORMALIZE TEXT
# -------------------------------------------------
def normalize_text(text):

    if not isinstance(text, str):
        return ""

    text = text.lower()

    # Preserve newlines
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


# -------------------------------------------------
# SECTION DETECTOR
# -------------------------------------------------
def detect_sections(text):

    if isinstance(text, dict):
        text = text.get("cleaned_text", "")

    if not isinstance(text, str):
        text = str(text)

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    lines = text.split("\n")

    sections = {
        "summary": [],
        "skills": [],
        "experience": [],
        "projects": [],
        "education": [],
        "certifications": [],
        "other": []
    }

    current_section = "other"

    for line in lines:

        line = line.strip()

        if not line:
            continue

        clean = normalize_text(line)

        found = False

        for section, keywords in SECTION_KEYWORDS.items():

            if any(keyword == clean for keyword in keywords):

                current_section = section
                found = True
                break

        if not found:
            sections[current_section].append(line)

    return sections


# -------------------------------------------------
# COMPATIBILITY FUNCTION
# -------------------------------------------------
def classify_sections(text):
    return detect_sections(text)


# -------------------------------------------------
# TEST
# -------------------------------------------------
if __name__ == "__main__":

    sample = """
Professional Summary
Python Developer with 3 years experience.

Skills
Python
SQL
Power BI

Experience
ABC Company
Software Engineer

Education
B.Tech
"""

    result = detect_sections(sample)

    for section, content in result.items():

        print("\n===================")
        print(section.upper())
        print("===================")

        for line in content:
            print(line)