from screening_ai.transcript_cleaner import process_audio_answers

audio_inputs = [
    "um i have 3 years experience in python",
    "uh currently working as backend developer",
    ""
]

results = process_audio_answers(audio_inputs)

print(results)