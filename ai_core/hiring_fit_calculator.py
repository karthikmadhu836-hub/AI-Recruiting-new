"""
Hiring Fit Calculator
Zecpath AI
"""


# ----------------------------------------
# Hiring Fit Classification
# ----------------------------------------
def calculate_hiring_fit(score):

    if score >= 85:
        category = "Excellent Fit"

    elif score >= 70:
        category = "Strong Fit"

    elif score >= 55:
        category = "Moderate Fit"

    else:
        category = "Low Fit"

    return {

        "hiring_fit_percentage": round(score, 2),

        "fit_category": category

    }


# ----------------------------------------
# Example
# ----------------------------------------
if __name__ == "__main__":

    print(
        calculate_hiring_fit(82.4)
    )