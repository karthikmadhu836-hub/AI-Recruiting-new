import os
import sys

# -------------------------------------------------
# Add project root
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------
# Imports
# -------------------------------------------------
from parsers.resume_extractor import extract_resume
from parsers.skill_extractor import extract_skills
from parsers.experience_parser import parse_experience
from parsers.jd_parser import parse_job_description

from ats_engine.semantic_matcher import (
    match_resume_to_jd,
    classify_match
)

# -------------------------------------------------
# Paths
# -------------------------------------------------

RESUME_FOLDER = "data/raw/resumes"
JD_FILE = "data/raw/job_descriptions/jd1.txt"

# -------------------------------------------------
# Load JD
# -------------------------------------------------

with open(JD_FILE, "r", encoding="utf-8") as f:
    jd_text = f.read()

jd_data = parse_job_description(jd_text)

# match_resume_to_jd expects this field
jd_data["job_description_text"] = jd_text

# -------------------------------------------------
# Compare every resume
# -------------------------------------------------

results = []

for file in os.listdir(RESUME_FOLDER):

    if not file.lower().endswith((".pdf", ".docx")):
        continue

    resume_path = os.path.join(RESUME_FOLDER, file)

    try:

        # -----------------------------
        # Resume Text
        # -----------------------------

        resume_text = extract_resume(resume_path)

        # -----------------------------
        # Skills
        # -----------------------------

        skills, confidence = extract_skills(resume_text)

        # -----------------------------
        # Experience
        # -----------------------------

        exp = parse_experience(resume_text)

        # -----------------------------
        # Build Resume Dictionary
        # -----------------------------

        resume_data = {

            "skills": skills,

            "experience": [
                {
                    "role": role
                }
                for role in exp["roles"]
            ],

            # Your project has no project parser
            "projects": [],

            "cleaned_text": resume_text
        }

        # -----------------------------
        # Match
        # -----------------------------

        similarity = match_resume_to_jd(
            resume_data,
            jd_data
        )

        final_score = similarity["final_similarity_score"]

        results.append(
            {
                "resume": file,
                "score": final_score,
                "classification": classify_match(final_score)
            }
        )

    except Exception as e:

        print(f"{file} -> ERROR -> {e}")

# -------------------------------------------------
# Sort
# -------------------------------------------------

results = sorted(
    results,
    key=lambda x: x["score"],
    reverse=True
)

# -------------------------------------------------
# Print Top 10
# -------------------------------------------------

print("\n" + "=" * 70)
print("TOP MATCHING RESUMES")
print("=" * 70)

for r in results[:10]:

    print(
        f"{r['resume']:35}"
        f"{r['score']:8.2f}%   "
        f"{r['classification']}"
    )

# -------------------------------------------------
# Save Ranking
# -------------------------------------------------

with open("ranked_candidates.csv", "w", encoding="utf-8") as f:

    f.write("Rank,Resume,Score,Classification\n")

    for i, r in enumerate(results, start=1):

        f.write(
            f"{i},{r['resume']},{r['score']},{r['classification']}\n"
        )

print("\nRanking saved to ranked_candidates.csv")