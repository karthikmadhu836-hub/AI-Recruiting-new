from screening_ai.question_loader import (
    load_questions
)


def get_screening_questions():

    questions = load_questions(
        "data/hr_screening_dataset.json"
    )

    return questions


def print_questions():

    questions = get_screening_questions()

    for q in questions:

        print(f"\n{q['question_id']}")
        print(q["question"])