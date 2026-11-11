"""
Day 65 - Production System Test
"""

from ai_core.final_production_system import production_pipeline


def test_production():

    result = production_pipeline(
        "C001",
        {
            "ats": 90,
            "screening": 78,
            "hr": 82,
            "technical": 88,
            "machine_test": 84
        }
    )

    assert result["status"] == "production_ready"
    assert result["decision"] in [
        "Selected",
        "Hold / Review",
        "Rejected"
    ]
    assert result["final_score"] <= 100


if __name__ == "__main__":
    test_production()
    print("Production system test passed.")