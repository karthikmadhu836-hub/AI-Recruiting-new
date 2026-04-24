import os
import json
import re

from parsers.resume_reader import extract_resume
from ats_engine.semantic_matcher import calculate_similarity
from scoring.ats_score import calculate_final_score
from scoring.weights import get_weights
from scoring.explainer import generate_explanation
from utils.fairness import normalize_text, mask_personal_info, normalize_score

# -------------------------------
# CONFIG
# -------------------------------
RESUME_FOLDER = "data/raw/resumes"
JD_FOLDER = "data/raw/job_descriptions"
OUTPUT_FILE = "data/outputs/final_pipeline_output.json"

CACHE_DIR = "data/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

RESUME_CACHE_FILE = os.path.join(CACHE_DIR, "resume_cache.json")
SIMILARITY_CACHE_FILE = os.path.join(CACHE_DIR, "similarity_cache.json")

# -------------------------------
# LOAD CACHE
# -------------------------------
def load_cache(path):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)

resume_cache = load_cache(RESUME_CACHE_FILE)
similarity_cache = load_cache(SIMILARITY_CACHE_FILE)

# -------------------------------
# CLEAN TEXT (NOISE HANDLING)
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9 ]', '', text)
    return text.strip()

# -------------------------------
# ENTITY EXTRACTION (SKILLS)
# -------------------------------
def extract_entities(text):
    keywords = [
        "python", "sql", "machine learning", "testing",
        "gmp", "laboratory", "analysis", "quality",
        "microbiology", "chemistry"
    ]
    return [k for k in keywords if k in text]

# -------------------------------
# MAIN PIPELINE
# -------------------------------
results = []

print("📂 Loading and caching resumes...")

for resume_file in os.listdir(RESUME_FOLDER):

    if not (resume_file.endswith(".pdf") or resume_file.endswith(".docx")):
        continue

    resume_path = os.path.join(RESUME_FOLDER, resume_file)

    try:
        # CACHE RESUME
        if resume_file in resume_cache:
            resume_text = resume_cache[resume_file]
        else:
            resume_text = extract_resume(resume_path)
            resume_text = clean_text(resume_text)
            resume_text = normalize_text(resume_text)
            resume_text = mask_personal_info(resume_text)

            # Skip bad resumes
            if len(resume_text) < 50:
                print(f"⚠️ Skipping low-quality resume: {resume_file}")
                continue

            resume_cache[resume_file] = resume_text
            save_cache(RESUME_CACHE_FILE, resume_cache)

    except Exception as e:
        print(f"❌ Error reading {resume_file}: {e}")
        continue

print(f"✅ Total resumes loaded: {len(resume_cache)}")

# -------------------------------
# PROCESS JOB DESCRIPTIONS
# -------------------------------
for jd_file in os.listdir(JD_FOLDER):

    if not jd_file.endswith(".txt"):
        continue

    print(f"\n🔍 Processing JD: {jd_file}")

    jd_path = os.path.join(JD_FOLDER, jd_file)

    try:
        with open(jd_path, "r", encoding="utf-8") as f:
            jd_text = f.read()

        jd_text = clean_text(jd_text)
        jd_text = normalize_text(jd_text)

    except Exception as e:
        print(f"❌ Error reading JD {jd_file}: {e}")
        continue

    jd_entities = extract_entities(jd_text)

    # -------------------------------
    # MATCH WITH RESUMES
    # -------------------------------
    for resume_file, resume_text in resume_cache.items():

        key = f"{resume_file}__{jd_file}"

        # SIMILARITY CACHE
        if key in similarity_cache:
            semantic_score = similarity_cache[key]
        else:
            semantic_score = calculate_similarity(resume_text, jd_text)
            similarity_cache[key] = semantic_score
            save_cache(SIMILARITY_CACHE_FILE, similarity_cache)

        # -------------------------------
        # ENTITY MATCHING
        # -------------------------------
        resume_entities = extract_entities(resume_text)

        if jd_entities:
            entity_score = len(set(resume_entities) & set(jd_entities)) / len(jd_entities)
        else:
            entity_score = 0

        # -------------------------------
        # FINAL SCORING
        # -------------------------------
        skill_score = semantic_score * 0.7 + entity_score * 0.3
        exp_score = 0.6
        edu_score = 0.5

        weights = get_weights()

        final_score = calculate_final_score(
            skill_score,
            exp_score,
            edu_score,
            semantic_score,
            weights
        )

        final_score = normalize_score(final_score)

        explanation = generate_explanation(
            skill_score,
            exp_score,
            edu_score,
            semantic_score,
            final_score
        )

        results.append({
            "resume": resume_file,
            "jd": jd_file,
            "score": final_score,
            "details": explanation
        })

# -------------------------------
# SORT RESULTS
# -------------------------------
results = sorted(results, key=lambda x: x["score"], reverse=True)

# -------------------------------
# SAVE OUTPUT
# -------------------------------
os.makedirs("data/outputs", exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=4)

print("\n🏁 OPTIMIZED ATS PIPELINE COMPLETED")
print(f"📁 Output saved to: {OUTPUT_FILE}")