"""
Day 61 - Audit Logging
"""

from datetime import datetime


def audit_log(action, user, candidate_id):

    return {

        "action": action,

        "user": user,

        "candidate_id": candidate_id,

        "timestamp": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":

    print(audit_log(
        "Decision Updated",
        "Recruiter01",
        "C1001"
    ))