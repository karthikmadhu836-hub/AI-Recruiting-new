from observability.logging import log_event


def test_ai_observability():

    log = log_event(
        "ATS",
        "testing",
        {}
    )

    assert "service" in log

    assert "timestamp" in log


if __name__ == "__main__":

    test_ai_observability()

    print("Day 61 Test Passed ✅")