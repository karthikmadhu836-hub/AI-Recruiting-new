"""
Day 61 - AI Logging System
"""

from datetime import datetime


def log_event(service, event_type, data):

    return {
        "service": service,
        "event_type": event_type,
        "data": data,
        "timestamp": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":

    print(log_event(
        "ATS",
        "score_generated",
        {"candidate": "C101", "score": 78}
    ))