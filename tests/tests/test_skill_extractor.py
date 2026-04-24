import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_reader import extract_resume
from parsers.skill_extractor import extract_skills

def test_skill_extraction():
    text = extract_resume("data/sample_resume.docx")

    skills, confidence = extract_skills(text)

    assert isinstance(skills, list)
    assert isinstance(confidence, dict)