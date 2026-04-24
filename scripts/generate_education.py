from parsers.resume_reader import extract_resume
from parsers.education_parser import parse_education
import json
import os

os.makedirs("data/processed", exist_ok=True)

text = extract_resume("data/sample_resume.docx")
edu = parse_education(text)

with open("data/processed/education_output.json", "w") as f:
    json.dump(edu, f, indent=4)

print("Education data saved!")