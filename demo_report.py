from screening_ai.report_generator import generate_screening_report

answers = [
    {
        "question_id": "Q1",
        "original_text": "I am a backend developer",

        "skills": ["python", "django"],

        "salary": "6 LPA",

        "availability": "Immediate",

        "is_vague": False,

        "off_topic": False
    }
]

scores = [
    {
        "question_id": "Q1",

        "final_score": 88
    }
]

behavior_reports = [
    {
        "communication_strength": "Strong"
    }
]

report = generate_screening_report(
    candidate_id="C123",
    job_id="J101",
    answers=answers,
    scores=scores,
    behavior_reports=behavior_reports
)

print(report)