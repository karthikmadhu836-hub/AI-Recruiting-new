import random


def simulate_candidate():

    return {
        "ats": random.randint(60, 90),
        "screening": random.randint(60, 85),
        "hr": random.randint(65, 90),
        "technical": random.randint(60, 95),
        "machine_test": random.randint(60, 95)
    }


def run_full_simulation(n=50):

    results = []

    for i in range(n):

        scores = simulate_candidate()

        avg_score = round(sum(scores.values()) / len(scores), 2)

        decision = "Selected" if avg_score >= 75 else "Rejected"

        results.append({
            "candidate_id": f"C{20000+i}",
            "scores": scores,
            "final_score": avg_score,
            "decision": decision
        })

    return results


if __name__ == "__main__":

    results = run_full_simulation()

    for candidate in results:
        print(candidate)