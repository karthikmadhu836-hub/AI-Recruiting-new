"""
Transcript Cleaner
Zecpath AI
"""

import re


def advanced_clean(text):

    text = text.lower()

    text = re.sub(

        r"\b(um|uh|like|you know)\b",

        "",

        text
    )

    text = re.sub(

        r"\b(\w+)( \1\b)+",

        r"\1",

        text
    )

    text = re.sub(

        r"[^\w\s]",

        "",

        text
    )

    text = re.sub(

        r"\s+",

        " ",

        text
    )

    return text.strip()


if __name__ == "__main__":

    sample = (

        "Um I I worked worked in Python!!"

    )

    print(

        advanced_clean(

            sample
        )
    )