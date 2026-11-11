"""
Zecpath AI
Security & Governance Module
Day 55 Deliverable
"""

from datetime import datetime

# ------------------------------------
# Role-Based Access Control (RBAC)
# ------------------------------------

ROLES = {
    "admin": {"read", "write", "delete"},
    "recruiter": {"read", "write"},
    "viewer": {"read"}
}


def has_access(role, action):
    """Check if a role can perform an action."""
    return action in ROLES.get(role, set())


# ------------------------------------
# Audit Logging
# ------------------------------------

def create_audit_log(event_type, candidate_id, user, details):
    """Generate an audit log entry."""
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "candidate_id": candidate_id,
        "user": user,
        "details": details
    }


# ------------------------------------
# Consent Validation
# ------------------------------------

def validate_consent(consent):
    """Verify candidate consent."""
    return bool(consent)


# ------------------------------------
# Data Retention Policy
# ------------------------------------

RETENTION_POLICY = {
    "resume": 90,
    "transcript": 60,
    "report": 120,
    "audit_log": 180
}


def get_retention_days(data_type):
    """Return retention period for a data type."""
    return RETENTION_POLICY.get(data_type, 0)


# ------------------------------------
# Example Usage
# ------------------------------------

if __name__ == "__main__":

    print("Admin Delete Access:",
          has_access("admin", "delete"))

    print("Viewer Write Access:",
          has_access("viewer", "write"))

    log = create_audit_log(
        event_type="decision_generated",
        candidate_id="C15001",
        user="Recruiter01",
        details={
            "decision": "Selected",
            "score": 82
        }
    )

    print("\nAudit Log")
    print(log)

    print("\nConsent:", validate_consent(True))
    print("Resume Retention:",
          get_retention_days("resume"), "days")