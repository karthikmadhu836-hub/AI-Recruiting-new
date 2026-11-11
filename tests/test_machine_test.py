from machine_test.evaluation_logic import (
    calculate_task_score,
    machine_test_pipeline
)


def test_machine_test():

    sample = {

        "candidate_id": "C5001",

        "code_snapshot": "print('Hello')",

        "execution_results": {

            "passed": 5,

            "total": 10,

            "runtime": 1.5

        },

        "attempts": 2,

        "time_taken": 25

    }

    result = machine_test_pipeline(sample)

    assert result["final_score"] > 0

    print("✅ Machine Test Passed")
    print(result)


if __name__ == "__main__":
    test_machine_test()