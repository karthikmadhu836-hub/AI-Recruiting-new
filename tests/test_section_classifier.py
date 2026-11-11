import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.section_classifier import classify_sections
from parsers.resume_extractor import extract_resume

def test_section_classifier():
    file_path = "data/sample_resume.docx"

    text = extract_resume(file_path)

    # ✅ Handle dict issue safely
    if isinstance(text, dict):
        text = text.get("cleaned_text", "")

    sections = classify_sections(text)

    assert isinstance(sections, dict)
    assert len(sections) > 0