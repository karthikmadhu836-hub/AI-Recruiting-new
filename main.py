import os
import json
import logging
from datetime import datetime

# -------------------------------
# IMPORT MODULES
# -------------------------------
from parsers.resume_extractor import extract_resume
from interview_ai.summary_generator import (
    generate_interview_summary
)
from parsers.section_classifier import detect_sections
from parsers.education_parser import (
    extract_education,
    extract_certifications
)
from parsers.experience_parser import parse_experience
from parsers.normalization import normalize_resume_text

from ats_engine.semantic_matcher import match_resume_to_jd
from ats_engine.ats_scorer import generate_candidate_score
from ats_engine.ranking_engine import ranking_pipeline
from ats_engine.skill_extractor import (
    extract_skills_and_confidence,
    extract_skills_with_confidence
)

from ats_engine.fairness_engine import (
    normalize_scores,
    mask_sensitive_data,
    generate_fair_score
)

from ats_engine.optimized_engine import (
    clean_noisy_resume,
    fast_skill_extract
)

from screening_ai.eligibility_engine import (
    evaluate_candidate
)

# -------------------------------
# LOGGING CONFIG
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("ATS_PIPELINE")

# -------------------------------
# CONFIG
# -------------------------------
RESUME_FOLDER = "data/raw/resumes"
JD_FOLDER = "data/raw/job_descriptions"
OUTPUT_FILE = "data/outputs/final_output.json"

CACHE_DIR = "data/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

RESUME_CACHE_FILE = os.path.join(
    CACHE_DIR,
    "resume_cache.json"
)

# -------------------------------
# CACHE FUNCTIONS
# -------------------------------
def load_cache(path):

    if os.path.exists(path):

        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)

        except Exception as e:
            logger.error(f"Cache Load Error: {e}")

    return {}


def save_cache(path, data):

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


resume_cache = load_cache(RESUME_CACHE_FILE)

# -------------------------------
# LOAD JOB DESCRIPTION
# -------------------------------
from parsers.jd_parser import parse_job_description

def load_jd(jd_path):

    try:
        # Read the JD text file
        with open(jd_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Parse the JD using your parser
        jd = parse_job_description(text)

        return {
            "job_title": jd.get("job_title", ""),
            "required_skills": jd.get("required_skills", []),
            "job_description_text": jd.get("cleaned_text", "")
        }

    except Exception as e:
        logger.error(f"Error loading JD {jd_path}: {e}")

        return {
            "job_title": "",
            "required_skills": [],
            "job_description_text": ""
        }

# -------------------------------
# PROCESS SINGLE RESUME
# -------------------------------
def process_resume(resume_file):

    logger.info(f"Processing Resume: {resume_file}")

    resume_path = os.path.join(
        RESUME_FOLDER,
        resume_file
    )

    print(f"\n📄 Reading Resume: {resume_path}")

    # -------------------------------
    # CACHE CHECK
    # -------------------------------
    if resume_file in resume_cache:

        logger.info(f"Loaded from cache: {resume_file}")

        return resume_cache[resume_file]

# -------------------------------
    # EXTRACT TEXT
    # -------------------------------
    import traceback

    try:
        data = extract_resume(resume_path)

        if isinstance(data, dict):
            text = data.get("cleaned_text", "")
        else:
            text = str(data)

    except Exception as e:
        print("\n========== RESUME EXTRACTION ERROR ==========")
        traceback.print_exc()
        print("=============================================\n")
        return ""

    # -------------------------------
    # EMPTY TEXT CHECK
    # -------------------------------
    if not text.strip():
        logger.warning(f"No text extracted from {resume_file}")
        return ""

    print(f"✅ Resume Processed | Length: {len(text)} characters")

    # -------------------------------
    # NORMALIZATION
    # -------------------------------
    text = normalize_resume_text(text)

    # -------------------------------
    # NOISE CLEANING
    # -------------------------------
    text = clean_noisy_resume(text)

    # -------------------------------
    # SECTION SEGMENTATION
    # -------------------------------
    sections = detect_sections(text)

    skills_sec = sections.get("skills", [])
    exp_sec = sections.get("experience", [])
    proj_sec = sections.get("projects", [])

    # Convert strings to lists
    if isinstance(skills_sec, str):
        skills_sec = [skills_sec]

    if isinstance(exp_sec, str):
        exp_sec = [exp_sec]

    if isinstance(proj_sec, str):
        proj_sec = [proj_sec]

    filtered_text = " ".join(skills_sec + exp_sec + proj_sec)

    if filtered_text.strip():
       text = filtered_text
    print(
        f"✅ Resume Processed | Length: {len(text)} characters"
    )

    # -------------------------------
    # SAVE CACHE
    # -------------------------------
    resume_cache[resume_file] = text

    save_cache(
        RESUME_CACHE_FILE,
        resume_cache
    )

    return text

# -------------------------------
# MAIN PIPELINE
# -------------------------------
def run_pipeline():

    print("\n========== ATS PIPELINE STARTED ==========\n")

    all_candidates = []

    logger.info("ATS PIPELINE STARTED")

    # -------------------------------
    # DEBUG CHECKS
    # -------------------------------
    print("Resume Folder:", RESUME_FOLDER)
    print("JD Folder:", JD_FOLDER)

    if not os.path.exists(RESUME_FOLDER):
        print(f"❌ Resume folder not found: {RESUME_FOLDER}")
        return []

    if not os.path.exists(JD_FOLDER):
        print(f"❌ JD folder not found: {JD_FOLDER}")
        return []

    #print("\n📄 Resume Files Found:")
    #print(os.listdir(RESUME_FOLDER))

    #print("\n📑 JD Files Found:")
    #print(os.listdir(JD_FOLDER))

    # -------------------------------
    # LOOP RESUMES
    # -------------------------------
    resume_files = ["sample_resume_1.pdf"]   # change to any resume you want

    for resume_file in resume_files:

        print(f"\n🔍 Checking File: {resume_file}")

        if not resume_file.lower().endswith(
            (".pdf", ".docx")
        ):
            print(f"⏭ Skipped: {resume_file}")
            continue

        print(f"✅ Processing Resume: {resume_file}")

        try:

            text = process_resume(resume_file)

            print("✔ Resume Extracted")

            # -------------------------------
            # SKILL EXTRACTION
            # -------------------------------
            skills, confidence = extract_skills_and_confidence(text)

            fast_skills = fast_skill_extract(text)

            skills = list(set(skills + fast_skills))

            print(f"✔ Skills Extracted: {len(skills)}")
            print(skills)
            print("===================================\n")
            print(
                f"✔ Skills Extracted: {len(skills)}"
            )

            # -------------------------------
            # EXPERIENCE
            # -------------------------------
            experience_data = parse_experience(
                text
            )
            print("\n========== EXPERIENCE ==========")
            print(experience_data)
            print("================================\n")
            print("✔ Experience Parsed")

            # -------------------------------
            # EDUCATION
            # -------------------------------
            education = extract_education(
                text
            )

            certifications = (
                extract_certifications(text)
            )

            print("✔ Education Parsed")

            # -------------------------------
            # LOOP JDS
            # -------------------------------
            for jd_file in os.listdir(JD_FOLDER):

                if not jd_file.endswith(".txt"):
                    continue

                print(
                    f"\n➡ Matching "
                    f"{resume_file}"
                    f" with "
                    f"{jd_file}"
                )

                jd_path = os.path.join(
                    JD_FOLDER,
                    jd_file
                )

                jd = load_jd(jd_path)
                print("\n========== JOB DESCRIPTION ==========")
                print("Job Title:", jd["job_title"])
                print("Required Skills:", jd["required_skills"])
                print("=====================================\n")
                # -------------------------------
                # SEMANTIC MATCHING
                # -------------------------------
                resume_obj = {

    "skills": skills,

    "experience": [

        {
            "role": role
        }

        for role in experience_data["roles"]

    ],

    "projects":[

        {

            "description": text

        }

    ],

    "resume_text": text

}
                print("\n========== RESUME OBJECT ==========")
                print(resume_obj)
                print("===================================\n")

                semantic_result = (
                    match_resume_to_jd(
                        resume_obj,
                        jd
                    )
                )
                print("\n==========================")
                print("Resume:", resume_file)

                print("\nResume Skills")
                print(skills)

                print("\nExperience")
                print(experience_data)

                print("\nResume Text Length")
                print(len(text))

                print("\nJD Skills")
                print(jd["required_skills"])

                print("\nJD Title")
                print(jd["job_title"])

                print("\nJD Text Length")
                print(len(jd["job_description_text"]))

                print("==========================")
                print("\n========== SEMANTIC RESULT ==========")
                print(semantic_result)
                print("=====================================\n")
                semantic_score = (
                    semantic_result.get(
                        "final_similarity_score",
                        0
                    )
                )

                print(
                    f"✔ Semantic Score: "
                    f"{semantic_score}"
                )

                # -------------------------------
                # COMPONENT SCORES
                # -------------------------------
                matched_skills = list(
                    set(skills)
                    &
                    set(jd["required_skills"])
                )

                
                # -------------------------------
                # SKILL SCORE
                # Percentage of required skills matched
                # -------------------------------
                required_skill_count = len(
                    jd["required_skills"]
                )

                if required_skill_count > 0:

                    skill_score = round(
                        (
                            len(matched_skills)
                            /
                            required_skill_count
                        ) * 100,
                        2
                    )

                else:

                     skill_score = 0

                # -------------------------------
                # EXPERIENCE SCORE
                # -------------------------------
                total_experience = experience_data.get(
                    "total_experience",
                     0
                )

                required = jd.get("min_experience_years", 0)

                if required == 0:

                    exp_score = 100

                else:

                   exp_score = min(

                       total_experience / required,

                         1

                    ) * 100

                # -------------------------------
                # EDUCATION SCORE
                # -------------------------------
                if education == jd.get("education_required", ""):

                    edu_score = 100

                else:

                    edu_score = 50

                # -------------------------------
                # DEBUG OUTPUT
                # -------------------------------
                print("\n========== SCORE DEBUG ==========")

                print("Matched Skills:", matched_skills)

                print(
                    f"Skill Score: {skill_score}"
                )

                print(
                    f"Experience Score: {exp_score}"
                )

                print(
                   f"Education Score: {edu_score}"
                )

                print("=================================\n")
                print("Matched Skills:", matched_skills)
                print("Skill Score:", skill_score)
                print("Experience Score:", exp_score)
                print("Education Score:", edu_score)
                print("Semantic Score:", semantic_score)
                # -------------------------------
                # ATS SCORE
                # -------------------------------
                score_data = generate_candidate_score(

                    {
                        "candidate_id": resume_file,
                        "skill_score": skill_score,
                        "experience_score": exp_score,
                        "education_score": edu_score,
                        "semantic_score": semantic_score
                    },

                    {
                        "job_title": jd["job_title"]
                    }
                )

                # -------------------------------
                # ELIGIBILITY ENGINE
                # -------------------------------
                eligibility_rules = {

                    "min_ats_score": 40,

                    "mandatory_skills":
                        jd["required_skills"],

                    "min_experience": 1,

                    "max_experience": 10,

                    "allowed_locations": [],

                    "availability_required": False
                }

                eligibility_result = evaluate_candidate(

                    {
                        "candidate_id": resume_file,

                        "final_score":
                            score_data["final_score"],

                        "skills": skills,

                        "total_experience":
                            experience_data.get(
                                "total_experience",
                                0
                            ),

                        "location": "Remote",

                        "available": True
                    },

                    eligibility_rules
                )

                # -------------------------------
                # STORE OUTPUT
                # -------------------------------
                candidate_entry = {

                    "candidate_id": resume_file,

                    "job_id": jd_file,

                    "job_title":
                        jd["job_title"],

                    "final_score":
                        score_data["final_score"],

                    "skill_score":
                        skill_score,

                    "experience_score":
                        exp_score,

                    "education_score":
                        edu_score,

                    "semantic_score":
                        semantic_score,

                    "eligibility":
                        eligibility_result,

                    "matched_skills":
                        matched_skills,

                    "all_skills":
                        skills,

                    "education":
                        education,

                    "certifications":
                        certifications,

                    "experience":
                        experience_data,

                    "semantic_details":
                        semantic_result,

                    "weights_used":
                        score_data["weights_used"],

                    "score_breakdown":
                        score_data["breakdown"],

                    "processed_at":
                        str(datetime.now())
                }

                all_candidates.append(candidate_entry)

        except Exception as e:

            logger.error(
                f"Error Processing "
                f"{resume_file}: {e}"
            )

    return all_candidates

# -------------------------------
# MAIN EXECUTION
# -------------------------------
def main():

    print("MAIN FUNCTION STARTED")

    candidates = run_pipeline()

    logger.info("Applying Fairness Engine")

    # -------------------------------
    # FAIRNESS ENGINE
    # -------------------------------
    candidates = normalize_scores(candidates)

    for c in candidates:

        mask_sensitive_data(c)

        generate_fair_score(c)

        # -------------------------------
    # RANKING
    # -------------------------------
    logger.info("Ranking Candidates")

    ranked = ranking_pipeline(candidates)

    # -------------------------------
    # AI INTERVIEW SUMMARY GENERATION
    # -------------------------------
    logger.info("Generating Interview Summaries")

    for candidate in ranked["top_candidates"]:

        try:

            summary = generate_interview_summary(

                candidate_id=candidate["candidate_id"],

                hr_scores=[
                    {
                        "question_id": "Q1",
                        "final_score": candidate["final_score"]
                    }
                ],

                communication={
                    "communication_score":
                        candidate["final_score"]
                },

                behavior={
                    "confidence": {
                        "confidence_score":
                            candidate["final_score"]
                    },
                    "behavioral_score":
                        candidate["final_score"],
                    "contradiction": False
                },

                answers=[
                    "Worked in a team environment"
                ]
            )

            candidate["interview_summary"] = summary

        except Exception as e:

            logger.error(
                f"Summary Generation Error: {e}"
            )

    # -------------------------------
    # SAVE OUTPUT
    # -------------------------------
    os.makedirs(
        "data/outputs",
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            ranked,
            f,
            indent=4
        )

    # -------------------------------
    # PRINT TOP CANDIDATES
    # -------------------------------
    print("\n🏆 TOP CANDIDATES\n")

    for c in ranked["top_candidates"]:

        print(
            f"{c['candidate_id']} "
            f"| Score: {c['final_score']} "
            f"| Status: {c['status']}"
        )

        if "interview_summary" in c:

            print(
                f"Recommendation: "
                f"{c['interview_summary']['decision']}"
            )

            print(
                f"Overall Score: "
                f"{c['interview_summary']['overall_score']}"
            )

            print(
                c["interview_summary"][
                    "natural_language_summary"
                ]
            )

            print("-" * 60)

    logger.info("PIPELINE COMPLETED")

    print(f"\n📁 Output Saved: {OUTPUT_FILE}")

    # -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    main()