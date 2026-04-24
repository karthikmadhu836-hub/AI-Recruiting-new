from parsers.resume_reader import extract_resume
from parsers.experience_parser import parse_experience
import json
import os

os.makedirs("data/processed", exist_ok=True)

text = extract_resume("data/sample_resume.docx")
exp = parse_experience(text)

with open("data/processed/experience_output.json", "w") as f:
    json.dump(exp, f, indent=4)

print("Experience data saved!")