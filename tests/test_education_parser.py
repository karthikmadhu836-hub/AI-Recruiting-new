import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_reader import extract_resume
from parsers.education_parser import parse_education

def test_education_parser():
    text = extract_resume("data/sample_resume.docx")

    edu = parse_education(text)

    assert "degree" in edu
    assert "certifications" in edu