from screening_ai.answer_engine import classify_intent


# -------------------------------
# Standalone Intent API
# -------------------------------
def get_intent(text):

    return classify_intent(text)