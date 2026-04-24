import os
import json

# -------------------------------
# CACHE FILE PATH
# -------------------------------
CACHE_DIR = "data/cache"
RESUME_CACHE_FILE = os.path.join(CACHE_DIR, "resume_cache.json")
SIMILARITY_CACHE_FILE = os.path.join(CACHE_DIR, "similarity_cache.json")

# Ensure cache directory exists
os.makedirs(CACHE_DIR, exist_ok=True)


# -------------------------------
# LOAD CACHE
# -------------------------------
def load_cache(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}


# -------------------------------
# SAVE CACHE
# -------------------------------
def save_cache(file_path, cache_data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(cache_data, f)


# -------------------------------
# RESUME CACHE FUNCTIONS
# -------------------------------
resume_cache = load_cache(RESUME_CACHE_FILE)

def get_cached_resume(resume_path, extract_function):
    """
    Returns cached resume text if available,
    otherwise extracts and stores it.
    """
    if resume_path in resume_cache:
        return resume_cache[resume_path]

    text = extract_function(resume_path)
    resume_cache[resume_path] = text
    save_cache(RESUME_CACHE_FILE, resume_cache)

    return text


# -------------------------------
# SIMILARITY CACHE FUNCTIONS
# -------------------------------
similarity_cache = load_cache(SIMILARITY_CACHE_FILE)

def get_cached_similarity(resume_id, jd_id, compute_function):
    """
    Cache similarity scores between resume and JD
    """
    key = f"{resume_id}__{jd_id}"

    if key in similarity_cache:
        return similarity_cache[key]

    score = compute_function()
    similarity_cache[key] = score
    save_cache(SIMILARITY_CACHE_FILE, similarity_cache)

    return score