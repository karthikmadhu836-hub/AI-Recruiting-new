import json
import random


def load_question_bank():
    with open("interview_ai/question_bank.json", "r", encoding="utf-8") as f:
        return json.load(f)


def generate_questions(role_type, experience_level):
    qb = load_question_bank()

    questions = []

    questions.extend(
        qb["categories"]["introduction"][experience_level]
    )

    for category in [
        "strengths_weaknesses",
        "teamwork",
        "career_goals",
        "availability"
    ]:
        questions.extend(
            qb["categories"][category]["common"]
        )

    questions.extend(
        qb["role_based"][role_type]
    )

    return random.sample(
        questions,
        min(6, len(questions))
    )


if __name__ == "__main__":
    qs = generate_questions(
        role_type="technical",
        experience_level="experienced"
    )

    print("\nGenerated Questions:\n")

    for i, q in enumerate(qs, start=1):
        print(f"{i}. {q}")