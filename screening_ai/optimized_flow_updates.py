# -------------------------------
# Adaptive Retry Logic
# -------------------------------
def adaptive_retry_logic(issue, retry_count):

    # Silence Handling
    if issue == "silence":

        if retry_count == 0:
            return "retry"

        elif retry_count == 1:
            return "simplify_question"

        else:
            return "skip_question"

    # Confusion Handling
    if issue == "confusion":
        return "clarify"

    # Repeat Handling
    if issue == "repeat":
        return "ask_example"

    return "next"


# -------------------------------
# Example Execution
# -------------------------------
if __name__ == "__main__":

    issues = [
        ("silence", 0),
        ("silence", 1),
        ("silence", 2),
        ("confusion", 0),
        ("repeat", 0)
    ]

    for issue, retry in issues:

        action = adaptive_retry_logic(issue, retry)

        print(
            f"Issue: {issue} | Retry: {retry} | Action: {action}"
        )