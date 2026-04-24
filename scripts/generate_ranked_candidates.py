import json
import os

from screening_ai.shortlisting import (
    rank_candidates,
    shortlist_candidates,
    get_top_candidates
)

# Load scores from Day 13
with open("data/outputs/final_scores.json", "r") as f:
    results = json.load(f)

# 1. Rank candidates
ranked = rank_candidates(results)

# 2. Apply dynamic shortlisting
shortlisted, review, rejected = shortlist_candidates(ranked)

# 3. Get top candidates per JD
top_candidates = get_top_candidates(ranked, top_n=5)

# Create output folder
os.makedirs("data/outputs", exist_ok=True)

# Save outputs
with open("data/outputs/ranked_candidates.json", "w") as f:
    json.dump(ranked, f, indent=4)

with open("data/outputs/shortlisted.json", "w") as f:
    json.dump(shortlisted, f, indent=4)

with open("data/outputs/review.json", "w") as f:
    json.dump(review, f, indent=4)

with open("data/outputs/rejected.json", "w") as f:
    json.dump(rejected, f, indent=4)

with open("data/outputs/top_candidates.json", "w") as f:
    json.dump(top_candidates, f, indent=4)

print("✅ Ranking, Shortlisting & Top Candidates Generated Successfully!")