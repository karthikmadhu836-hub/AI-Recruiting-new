import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from screening_ai.report_generator import generate_screening_report


def run_demo():
    candidate_id = "C1001"
    job_id = "J2001"

    answers = [
        {
            "question_id": "Q1",
            "original_text": "I have 3 years experience in Python",
            "skills": ["Python"],
            "availability": "Immediate",
            "salary": "6 LPA",
            "is_vague": False,
            "off_topic": False
        }
    ]

    scores = [
        {
            "question_id": "Q1",
            "final_score": 85
        }
    ]

    behavior_reports = [
        {
            "communication_strength": "Strong"
        }
    ]

    report = generate_screening_report(
        candidate_id,
        job_id,
        answers,
        scores,
        behavior_reports
    )

    print("\n=== AI Screening Report ===\n")
    print(report)


if __name__ == "__main__":
    run_demo()