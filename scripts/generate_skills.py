from parsers.resume_reader import extract_resume
from parsers.skill_extractor import extract_skills
import json

text = extract_resume("data/sample_resume.docx")
skills, confidence = extract_skills(text)

output = {
    "skills": skills,
    "confidence": confidence
}

with open("data/processed/skills_output.json", "w") as f:
    json.dump(output, f, indent=4)

print("Skills extracted and saved!")