import json
import os

from parsers.resume_reader import extract_resume
from ats_engine.semantic_matcher import calculate_similarity

# -----------------------------
# TEXT CLEANING FUNCTION
# -----------------------------
def clean_text(text):
    return text.lower().replace("\n", " ").strip()


# -----------------------------
# KEYWORD BOOST FUNCTION
# -----------------------------
def keyword_boost(resume_text):
    important_keywords = [
        "quality", "lab", "testing", "gmp",
        "analysis", "laboratory", "microbiology",
        "chemistry", "validation", "compliance"
    ]

    bonus = 0
    for word in important_keywords:
        if word in resume_text:
            bonus += 0.05  # small boost per keyword

    return bonus


# -----------------------------
# LOAD GROUND TRUTH
# -----------------------------
with open("data/evaluation/ground_truth.json", "r") as f:
    ground_truth = json.load(f)

results = []

# -----------------------------
# MAIN LOOP
# -----------------------------
for jd_file, labels in ground_truth.items():

    print(f"\n🔍 Evaluating for JD: {jd_file}")

    jd_path = f"data/evaluation/{jd_file}"

    if not os.path.exists(jd_path):
        print(f"❌ JD not found: {jd_path}")
        continue

    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text = clean_text(f.read())

    resume_scores = []

    # -----------------------------
    # CALCULATE SCORES
    # -----------------------------
    for resume in labels["relevant"] + labels["irrelevant"]:

        resume_path = f"data/evaluation/resumes/{resume}"

        if not os.path.exists(resume_path):
            print(f"❌ Resume not found: {resume_path}")
            continue

        try:
            resume_text = clean_text(extract_resume(resume_path))
        except Exception as e:
            print(f"❌ Error reading {resume}: {e}")
            continue

        similarity = calculate_similarity(resume_text, jd_text)
        boost = keyword_boost(resume_text)

        final_score = similarity + boost

        resume_scores.append((resume, final_score))

        print(f"{resume} → Similarity: {similarity:.2f} + Boost: {boost:.2f} = Final: {final_score:.2f}")

    # -----------------------------
    # TOP-K SELECTION (IMPORTANT)
    # -----------------------------
    resume_scores = sorted(resume_scores, key=lambda x: x[1], reverse=True)

    top_k = len(labels["relevant"])  # dynamically match ground truth
    top_resumes = [r[0] for r in resume_scores[:top_k]]

    print(f"\n🏆 Top {top_k} selected: {top_resumes}")

    # -----------------------------
    # EVALUATION
    # -----------------------------
    for resume, score in resume_scores:

        predicted = resume in top_resumes
        actual = resume in labels["relevant"]

        results.append((predicted, actual))


# -----------------------------
# METRICS CALCULATION
# -----------------------------
tp = sum(1 for p, a in results if p and a)
fp = sum(1 for p, a in results if p and not a)
fn = sum(1 for p, a in results if not p and a)

precision = tp / (tp + fp) if (tp + fp) else 0
recall = tp / (tp + fn) if (tp + fn) else 0

# -----------------------------
# FINAL OUTPUT
# -----------------------------
print("\n📊 FINAL RESULTS")
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))