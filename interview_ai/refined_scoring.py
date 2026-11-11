"""
Refined Scoring Engine
Zecpath AI
"""


def normalize_scores(scores):

    if not scores:

        return []

    min_s = min(scores)

    max_s = max(scores)

    if max_s == min_s:

        return scores

    normalized = []

    for s in scores:

        value = (

            (s - min_s)

            /

            (max_s - min_s)

        ) * 100

        normalized.append(

            round(value, 2)
        )

    return normalized


def reduce_bias(

    score,

    confidence
):

    adjusted = (

        score * 0.90

        +

        confidence * 0.10
    )

    return round(

        adjusted,

        2
    )


def refined_score_pipeline(

    scores,

    confidence_scores
):

    normalized = normalize_scores(

        scores
    )

    final_scores = []

    for s, c in zip(

        normalized,

        confidence_scores
    ):

        final_scores.append(

            reduce_bias(

                s,

                c
            )
        )

    return final_scores


if __name__ == "__main__":

    print(

        refined_score_pipeline(

            [60, 72, 88],

            [75, 80, 90]

        )
    )