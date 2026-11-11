import re


def normalize_transcript(text):

    text = text.lower()

    # Remove filler words
    fillers = [
        "um",
        "uh",
        "like",
        "you know"
    ]

    for f in fillers:

        text = re.sub(
            rf"\b{f}\b",
            "",
            text
        )

    # Remove repeated spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()