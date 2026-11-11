from screening_ai.scoring_engine import screening_scoring_pipeline


answers = [
    {
        "question_id": "Q3",
        "original_text": "I have 3 years experience in Python",
        "intent": "experience",
        "skills": ["python"],
        "experience_years": 3,
        "availability": "Immediate",
        "off_topic": False,
        "is_vague": False
    }
]

intent_map = {
    "Q3": "experience"
}

result = screening_scoring_pipeline(
    answers,
    intent_map
)

print(result)