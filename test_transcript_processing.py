from screening_ai.transcript_processor import (
    process_transcript
)

raw_answers = [

    {
        "question_id": "Q1",

        "text": "Um I am a Python developer",

        "confidence": 0.95
    },

    {
        "question_id": "Q2",

        "text": "Uh I have 3 years experience",

        "confidence": 0.91
    }
]

results = process_transcript(raw_answers)

print(results)