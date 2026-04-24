from parsers.resume_reader import extract_resume
from parsers.section_classifier import classify_sections
import json

# Step 1: Read resume
text = extract_resume("data/sample_resume.docx")

# Step 2: Classify sections
sections = classify_sections(text)

# Step 3: Save output
with open("data/sectioned_resumes/resume1.json", "w") as f:
    json.dump(sections, f, indent=4)

print("Sectioned resume saved!")