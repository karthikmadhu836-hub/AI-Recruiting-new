# tests/test_ats_accuracy.py

def evaluate_accuracy(ai_results, hr_results):

    tp = fp = fn = tn = 0

    for ai, hr in zip(ai_results, hr_results):

        # True Positive
        if ai == "Shortlisted" and hr == "Shortlisted":
            tp += 1

        # False Positive
        elif ai == "Shortlisted" and hr == "Rejected":
            fp += 1

        # False Negative
        elif ai == "Rejected" and hr == "Shortlisted":
            fn += 1

        # True Negative
        else:
            tn += 1

    # -------------------------
    # METRICS
    # -------------------------
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0

    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    accuracy = (tp + tn) / len(ai_results) if len(ai_results) > 0 else 0

    f1_score = (
        2 * (precision * recall) / (precision + recall)
        if (precision + recall) > 0 else 0
    )

    # -------------------------
    # OUTPUT
    # -------------------------
    return {
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "true_negative": tn,
        "precision": round(precision * 100, 2),
        "recall": round(recall * 100, 2),
        "accuracy": round(accuracy * 100, 2),
        "f1_score": round(f1_score * 100, 2)
    }


# ---------------------------------
# SAMPLE TEST
# ---------------------------------
if __name__ == "__main__":

    ai_results = [
        "Shortlisted",
        "Shortlisted",
        "Rejected",
        "Shortlisted",
        "Rejected"
    ]

    hr_results = [
        "Shortlisted",
        "Rejected",
        "Rejected",
        "Shortlisted",
        "Shortlisted"
    ]

    result = evaluate_accuracy(ai_results, hr_results)

    print("\nATS Accuracy Metrics\n")

    for key, value in result.items():
        print(f"{key}: {value}")