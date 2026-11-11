from ats_engine.ats_scorer import generate_candidate_score

def test_ats_scorer():
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

    assert result["final_score"] > 0