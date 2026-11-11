from tests.full_simulation import run_full_simulation


def test_full_simulation():

    results = run_full_simulation(10)

    assert len(results) == 10

    for candidate in results:
        assert "scores" in candidate
        assert "decision" in candidate
        assert "final_score" in candidate


if __name__ == "__main__":
    test_full_simulation()
    print("✅ Day 56 Full System Simulation Test Passed")