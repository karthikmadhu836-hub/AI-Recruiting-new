import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_reader import extract_resume
from parsers.section_classifier import classify_sections

def test_section_classifier():
    file_path = "data/sample_resume.docx"

    text = extract_resume(file_path)
    sections = classify_sections(text)

    assert "skills" in sections
    assert len(sections["skills"]) >= 0