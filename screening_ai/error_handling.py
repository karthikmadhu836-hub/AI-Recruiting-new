# -------------------------------
# Detect Conversation Issues
# -------------------------------
def detect_issue(answer):

    # Silence
    if not answer or len(answer.strip()) == 0:

        return "silence"

    # Confusion
    if len(answer.split()) < 2:

        return "confusion"

    # Repeat Detection
    if len(set(answer.split())) < len(answer.split()) / 2:

        return "repeat"

    return "valid"


# -------------------------------
# Retry Messages
# -------------------------------
RETRY_MESSAGES = {

    "silence":
        "Sorry, I didn't hear anything. Could you please respond?",

    "confusion":
        "Let me clarify the question for you.",

    "repeat":
        "Could you provide more details?"
}


# -------------------------------
# Response Handler
# -------------------------------
def handle_response(state_machine, answer):

    issue = detect_issue(answer)

    if issue == "silence":

        state_machine.handle_silence()

    elif issue == "confusion":

        state_machine.handle_confusion()

    elif issue == "repeat":

        state_machine.handle_repeat()

    else:

        state_machine.next()

    return issue