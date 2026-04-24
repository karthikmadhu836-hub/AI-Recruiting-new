import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_reader import extract_resume
from parsers.experience_parser import parse_experience

def test_experience_parser():
    text = extract_resume("data/sample_resume.docx")

    exp = parse_experience(text)

    assert "total_experience_years" in exp