import os
import re
from pypdf import PdfReader
from docx import Document

# -------------------------------------------------
# PDF Reader
# -------------------------------------------------
def extract_text_from_pdf(file_path):
    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text


# -------------------------------------------------
# DOCX Reader
# -------------------------------------------------
def extract_text_from_docx(file_path):

    doc = Document(file_path)

    return "\n".join(
        para.text for para in doc.paragraphs
    )


# -------------------------------------------------
# CLEAN TEXT
# -------------------------------------------------
def clean_text(text):

    if not text:
        return ""

    # Remove strange unicode
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Keep letters, numbers and NEWLINES
    text = re.sub(
        r"[^a-zA-Z0-9\s\.,:/()\-]",
        " ",
        text
    )

    # Normalize spaces WITHOUT removing newlines
    text = re.sub(r"[ \t]+", " ", text)

    # Remove too many blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()


# -------------------------------------------------
# NORMALIZE HEADINGS
# -------------------------------------------------
def normalize_sections(text):

    replacements = {

        "WORK EXPERIENCE": "Experience",
        "PROFESSIONAL EXPERIENCE": "Experience",
        "EMPLOYMENT HISTORY": "Experience",

        "EDUCATION DETAILS": "Education",
        "ACADEMIC DETAILS": "Education",

        "SKILLS SET": "Skills",
        "TECHNICAL SKILLS": "Skills",

        "PROJECT EXPERIENCE": "Projects",

        "PROFILE": "Summary",
        "CAREER OBJECTIVE": "Summary"
    }

    for old, new in replacements.items():

        text = re.sub(
            old,
            new,
            text,
            flags=re.IGNORECASE
        )

    return text


# -------------------------------------------------
# MAIN EXTRACTION
# -------------------------------------------------
def extract_resume(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":

        raw_text = extract_text_from_pdf(file_path)

    elif ext == ".docx":

        raw_text = extract_text_from_docx(file_path)

    else:

        raise ValueError("Unsupported file format")

    cleaned = clean_text(raw_text)

    normalized = normalize_sections(cleaned)

    return normalized


# -------------------------------------------------
# TEST
# -------------------------------------------------
if __name__ == "__main__":

    resume_path = "data/raw/resumes/sample_resume_1.pdf"

    if not os.path.exists(resume_path):

        print("Resume not found.")

    else:

        text = extract_resume(resume_path)

        print("=" * 80)
        print(text)
        print("=" * 80)