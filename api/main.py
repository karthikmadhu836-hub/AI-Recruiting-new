from fastapi import FastAPI, UploadFile, File
import shutil
import os
import json

# IMPORT YOUR ATS MODULES
from parsers.resume_extractor import extract_resume
from parsers.education_parser import extract_education
from parsers.experience_parser import parse_experience

from ats_engine.skill_extractor import extract_skills_with_confidence
from ats_engine.semantic_matcher import match_resume_to_jd
from ats_engine.ats_scorer import generate_candidate_score
from ats_engine.ranking_engine import ranking_pipeline

app = FastAPI(
    title="Zecpath ATS API",
    version="1.0"
)

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------------
# HOME ROUTE
# -----------------------------------
@app.get("/")
def home():
    return {
        "message": "Zecpath ATS API Running"
    }


# -----------------------------------
# RESUME UPLOAD API
# -----------------------------------
@app.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "message": "Resume uploaded successfully",
        "resume_path": file_path
    }


# -----------------------------------
# RESUME PARSING API
# -----------------------------------
@app.post("/resume/parse")
def parse_resume(resume_path: str):

    text = extract_resume(resume_path)

    education = extract_education(text)
    experience = parse_experience(text)
    skills = extract_skills_with_confidence(text)

    return {
        "status": "completed",
        "parsed_profile": {
            "education": education,
            "experience": experience,
            "skills": skills
        }
    }


# -----------------------------------
# ATS SCORING API
# -----------------------------------
@app.post("/ats/score")
def ats_score():

    # SAMPLE DATA
    candidate = {
        "candidate_id": "C123",
        "skill_score": 90,
        "experience_score": 85,
        "education_score": 80,
        "semantic_score": 88
    }

    job = {
        "job_title": "Backend Developer"
    }

    result = generate_candidate_score(candidate, job)

    return result


# -----------------------------------
# RANKING API
# -----------------------------------
@app.post("/ats/rank")
def rank():

    candidates = [
        {"candidate_id": "C1", "final_score": 88},
        {"candidate_id": "C2", "final_score": 72},
        {"candidate_id": "C3", "final_score": 45}
    ]

    ranked = ranking_pipeline(candidates)

    return ranked