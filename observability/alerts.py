"""
Day 61 - Alert Rules
"""


def check_alerts(metrics):

    alerts = []

    if metrics["avg_latency"] > 2:

        alerts.append("High latency detected")

    if metrics["failure_rate"] > 0.10:

        alerts.append("Failure rate exceeded")

    if metrics["success_rate"] < 0.90:

        alerts.append("Low success rate")

    return alerts


if __name__ == "__main__":

    sample = {

        "avg_latency": 2.5,

        "failure_rate": 0.15,

        "success_rate": 0.80
    }

    print(check_alerts(sample))