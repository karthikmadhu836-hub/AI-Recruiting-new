def json_to_text(resume_json):
    parts = []

    # Summary
    parts.append(resume_json.get("summary", ""))

    # Skills
    skills = [s["skill_name"] for s in resume_json.get("skills", [])]
    parts.append(" ".join(skills))

    # Experience
    for exp in resume_json.get("experience", []):
        parts.append(exp.get("role", ""))
        parts.extend(exp.get("responsibilities", []))

    # Education
    for edu in resume_json.get("education", []):
        parts.append(edu.get("degree", ""))
        parts.append(edu.get("field", ""))

    # Projects
    for proj in resume_json.get("projects", []):
        parts.append(proj.get("description", ""))

    return " ".join(parts).lower()