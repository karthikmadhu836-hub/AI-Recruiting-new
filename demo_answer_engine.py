from screening_ai.answer_engine import process_answer


answer = "I have 3 years experience in Python and Django"

result = process_answer("Q3", answer)

print(result)