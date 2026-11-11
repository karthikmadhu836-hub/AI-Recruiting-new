"""
Followup Stability Logic
Zecpath AI
"""


def stable_followup(

    answer_quality,

    retry_count
):

    if retry_count >= 2:

        return "skip"

    if answer_quality in [

        "empty",

        "too_short"

    ]:

        return "clarify"

    if answer_quality == "uncertain":

        return "simplify"

    return "continue"


if __name__ == "__main__":

    print(

        stable_followup(

            "too_short",

            1
        )
    )