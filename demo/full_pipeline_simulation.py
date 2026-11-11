# demo/full_pipeline_simulation.py

import json
from pathlib import Path


def load_candidate_profiles():
    path = Path(__file__).parent / "candidate_profiles.json"

    with open(path, "r") as file:
        return json.load(file)


def run_demo_pipeline(candidate_id):

    scores = {
        "C001": {"final": 85, "decision": "Selected"},
        "C002": {"final": 68, "decision": "Hold / Review"},
        "C003": {"final": 45, "decision": "Rejected"},
    }

    return {
        "candidate_id": candidate_id,
        "result": scores.get(candidate_id)
    }


if __name__ == "__main__":

    candidates = load_candidate_profiles()

    for candidate in candidates:
        print(run_demo_pipeline(candidate["candidate_id"]))