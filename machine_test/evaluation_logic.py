"""
Machine Test Evaluation Engine
Zecpath AI
"""

# ----------------------------------------
# Correctness Score
# ----------------------------------------

def correctness_score(passed, total):

    if total == 0:
        return 0.0

    return passed / total


# ----------------------------------------
# Runtime Efficiency
# ----------------------------------------

def efficiency_score(runtime):

    if runtime < 1:
        return 1.0

    elif runtime < 2:
        return 0.7

    return 0.4


# ----------------------------------------
# Code Quality
# ----------------------------------------

def code_quality_score(code):

    lines = len(code.splitlines())

    if lines < 20:
        return 1.0

    elif lines < 50:
        return 0.7

    return 0.4


# ----------------------------------------
# Problem Solving
# ----------------------------------------

def problem_solving_score(attempts):

    if attempts == 1:
        return 1.0

    elif attempts <= 3:
        return 0.7

    return 0.4


# ----------------------------------------
# Time Score
# ----------------------------------------

def time_score(time_taken, limit):

    ratio = time_taken / limit

    if ratio <= 0.5:
        return 1.0

    elif ratio <= 1.0:
        return 0.7

    return 0.4


# ----------------------------------------
# Task Score
# ----------------------------------------

def calculate_task_score(
    passed,
    total,
    runtime,
    code,
    attempts
):

    correctness = correctness_score(
        passed,
        total
    )

    efficiency = efficiency_score(
        runtime
    )

    quality = code_quality_score(
        code
    )

    problem = problem_solving_score(
        attempts
    )

    final = (

        correctness * 0.40 +

        efficiency * 0.20 +

        quality * 0.20 +

        problem * 0.20

    )

    return {

        "task_score": round(final * 100, 2),

        "breakdown": {

            "correctness": round(correctness, 2),

            "efficiency": round(efficiency, 2),

            "code_quality": round(quality, 2),

            "problem_solving": round(problem, 2)

        }

    }


# ----------------------------------------
# Machine Test Pipeline
# ----------------------------------------

def machine_test_pipeline(data):

    score = calculate_task_score(

        data["execution_results"]["passed"],

        data["execution_results"]["total"],

        data["execution_results"]["runtime"],

        data["code_snapshot"],

        data["attempts"]

    )

    time_factor = time_score(

        data["time_taken"],

        30

    )

    final_score = (

        score["task_score"] * 0.80 +

        (time_factor * 100) * 0.20

    )

    decision = (

        "Excellent"

        if final_score >= 85

        else

        "Good Performance"

        if final_score >= 70

        else

        "Needs Improvement"

    )

    return {

        "candidate_id": data["candidate_id"],

        "task_score": score["task_score"],

        "time_score": round(time_factor * 100, 2),

        "final_score": round(final_score, 2),

        "decision": decision,

        "details": score["breakdown"]

    }


# ----------------------------------------
# Example Execution
# ----------------------------------------

if __name__ == "__main__":

    sample = {

        "candidate_id": "C5001",

        "code_snapshot": "print('Hello World')",

        "execution_results": {

            "passed": 8,

            "total": 10,

            "runtime": 1.3

        },

        "attempts": 2,

        "time_taken": 24

    }

    print(

        machine_test_pipeline(sample)

    )