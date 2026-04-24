import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_reader import extract_resume
from ats_engine.semantic_matcher import calculate_similarity

def test_similarity():
    resume = extract_resume("data/sample_resume.docx")

    jd_folder = "data/raw/job_descriptions"

    jd_file = None
    for file in os.listdir(jd_folder):
        if file.endswith(".txt"):
            jd_file = os.path.join(jd_folder, file)
            break

    assert jd_file is not None, "No JD file found"

    with open(jd_file, "r") as f:
        jd = f.read()

    score = calculate_similarity(resume, jd)

    assert score >= 0