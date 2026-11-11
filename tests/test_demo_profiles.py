import json
from pathlib import Path

from demo.full_pipeline_simulation import run_demo_pipeline


def test_candidate_profiles():

    path = Path(__file__).parent.parent / "demo" / "candidate_profiles.json"

    with open(path) as f:
        candidates = json.load(f)

    for candidate in candidates:

        result = run_demo_pipeline(candidate["candidate_id"])

        assert result["result"]["decision"] == candidate["expected_decision"]

        assert result["result"]["final"] == candidate["expected_score"]