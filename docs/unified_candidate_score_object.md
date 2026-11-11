# Unified Candidate Score Object – Zecpath

## Objective

Represent the complete evaluation of a candidate by combining scores from all hiring stages into a single transparent object.

---

# Candidate Score Structure

```json
{
    "candidate_id": "C9001",

    "scores": {

        "ats": 75,

        "screening": 70,

        "hr": 80,

        "technical": 85,

        "machine_test": 78
    },

    "weights": {

        "ats": 0.15,

        "screening": 0.10,

        "hr": 0.15,

        "technical": 0.35,

        "machine_test": 0.25
    },

    "final_score": 80.10,

    "decision": "Hire",

    "hiring_fit": {

        "hiring_fit_percentage": 80.10,

        "fit_category": "Strong Fit"

    }
}
```

---

# Explainable Score Breakdown

```json
{
    "explanation": {

        "ats": "Good resume-job match",

        "screening": "Clear responses with minor gaps",

        "hr": "Strong communication and confidence",

        "technical": "High technical depth",

        "machine_test": "Good practical coding performance"
    }
}
```

---

# Hiring Decision Levels

| Final Score | Decision |
|-------------|----------|
| 85–100 | Excellent Fit |
| 70–84 | Strong Fit |
| 55–69 | Moderate Fit |
| Below 55 | Low Fit |

---

# Final Score Formula

```
Final Score =

(ATS × Weight)

+

(Screening × Weight)

+

(HR × Weight)

+

(Technical × Weight)

+

(Machine Test × Weight)
```

---

# Role-Based Weight Example

| Stage | Weight |
|--------|-------:|
| ATS | 20% |
| Screening | 15% |
| HR Interview | 20% |
| Technical Interview | 25% |
| Machine Test | 20% |

---

# Benefits

- Combines every hiring stage
- Recruiter-friendly
- Explainable AI scoring
- Consistent candidate comparison

---

# Future Improvements

- Dynamic weight optimization
- ML-based scoring
- Continuous learning from hiring outcomes