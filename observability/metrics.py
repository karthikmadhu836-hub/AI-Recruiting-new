"""
Day 61 - AI Metrics
"""


def calculate_metrics(success, total, response_times):

    success_rate = success / total if total else 0

    average_latency = (
        sum(response_times) / len(response_times)
        if response_times else 0
    )

    failure_rate = (
        (total - success) / total
        if total else 0
    )

    return {

        "success_rate": round(success_rate, 2),

        "failure_rate": round(failure_rate, 2),

        "avg_latency": round(average_latency, 2)
    }


if __name__ == "__main__":

    print(calculate_metrics(
        95,
        100,
        [1.1, 1.5, 0.9, 1.3]
    ))