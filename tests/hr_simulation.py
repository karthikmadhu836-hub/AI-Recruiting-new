import random
import json
import os

# ---------------------------------
# CREATE OUTPUT DIRECTORY
# ---------------------------------
os.makedirs(
    "data/outputs",
    exist_ok=True
)

# ---------------------------------
# Candidate Simulation
# ---------------------------------
def simulate_candidate(candidate_type):

    score_ranges = {
        "Confident": (80, 95),
        "Hesitant": (55, 70),
        "Inexperienced": (50, 65),
        "Overqualified": (75, 90)
    }

    ai_score = random.randint(
        score_ranges[candidate_type][0],
        score_ranges[candidate_type][1]
    )

    human_score = ai_score + random.randint(-5, 5)

    # AI Decision
    if ai_score >= 75:
        ai_decision = "Strong Hire"

    elif ai_score >= 55:
        ai_decision = "Consider"

    else:
        ai_decision = "Reject"

    # Human Decision
    if human_score >= 75:
        human_decision = "Strong Hire"

    elif human_score >= 55:
        human_decision = "Consider"

    else:
        human_decision = "Reject"

    return {
        "candidate_type": candidate_type,
        "ai_score": ai_score,
        "human_score": human_score,
        "decision_ai": ai_decision,
        "decision_human": human_decision
    }


# ---------------------------------
# Run Simulation
# ---------------------------------
def run_simulation():

    results = []

    # 10 Confident
    for _ in range(10):
        results.append(
            simulate_candidate(
                "Confident"
            )
        )

    # 10 Hesitant
    for _ in range(10):
        results.append(
            simulate_candidate(
                "Hesitant"
            )
        )

    # 10 Inexperienced
    for _ in range(10):
        results.append(
            simulate_candidate(
                "Inexperienced"
            )
        )

    # 10 Overqualified
    for _ in range(10):
        results.append(
            simulate_candidate(
                "Overqualified"
            )
        )

    return results


# ---------------------------------
# Accuracy Calculation
# ---------------------------------
def calculate_accuracy(results):

    matches = 0

    for r in results:

        if r["decision_ai"] == r["decision_human"]:
            matches += 1

    accuracy = (
        matches / len(results)
    ) * 100

    return round(accuracy, 2)


# ---------------------------------
# Main
# ---------------------------------
if __name__ == "__main__":

    results = run_simulation()

    accuracy = calculate_accuracy(
        results
    )

    print("\n========== HR INTERVIEW TEST REPORT ==========\n")

    print(
        f"Total Candidates Tested: {len(results)}"
    )

    print(
        f"Decision Accuracy: {accuracy}%"
    )

    print("\nSample Candidates:\n")

    for candidate in results[:5]:

        print(candidate)

    # ---------------------------------
    # SAVE REPORT
    # ---------------------------------
    with open(
        "data/outputs/hr_test_report.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=4
        )

    print(
        "\n✅ Report Saved Successfully"
    )

    print(
        "📁 data/outputs/hr_test_report.json"
    )