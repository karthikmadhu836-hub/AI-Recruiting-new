import json

from screening_ai.conversation_engine import ConversationStateMachine

from screening_ai.error_handling import detect_issue


flow = json.load(
    open(
        "screening_ai/conversation_flow.json",
        "r",
        encoding="utf-8"
    )
)

engine = ConversationStateMachine(flow)

while not engine.is_end():

    question = engine.get_question()

    print("\nAI:", question)

    answer = input("User: ")

    issue = detect_issue(answer)

    if issue == "silence":

        engine.handle_silence()

    elif issue == "confusion":

        engine.handle_confusion()

    elif issue == "repeat":

        engine.handle_repeat()

    else:

        engine.next()

print("\nConversation Ended")