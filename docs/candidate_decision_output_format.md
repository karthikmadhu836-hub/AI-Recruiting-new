# Candidate Decision Output Format – Zecpath AI

## Objective

Provide a standardized, explainable decision object after evaluating all interview stages and applying risk adjustments.

---

# Sample Decision Output

```json
{
  "candidate_id": "C10001",
  "final_score": 82,
  "adjusted_score": 75,
  "decision": "Selected",
  "confidence_score": 88,
  "risks": {
    "behavior": "Low Risk",
    "integrity": "Moderate Risk"
  },
  "explanation": {
    "reason": "Strong overall performance with minor integrity concerns",
    "strengths": [
      "High technical score",
      "Good communication"
    ],
    "weaknesses": [
      "Minor distraction signals"
    ]
  }
}
```

---

# Decision Categories

| Decision | Description |
|----------|-------------|
| Selected | Candidate meets hiring criteria and has acceptable risk. |
| Hold / Review | Candidate requires manual review before a final decision. |
| Rejected | Candidate does not meet score or risk requirements. |

---

# Decision Process

1. Collect final aggregated hiring score.
2. Apply behavior and integrity risk penalties.
3. Compare adjusted score with decision thresholds.
4. Calculate confidence score.
5. Generate explainable output.
6. Produce final recommendation.

---

# Decision Thresholds

| Adjusted Score | Decision |
|---------------:|----------|
| 80–100 | Selected |
| 60–79 | Hold / Review |
| Below 60 | Rejected |

---

# Confidence Score

The confidence score reflects the consistency of candidate performance across evaluation stages.

- High Confidence: 85–100
- Medium Confidence: 70–84
- Low Confidence: Below 70

---

# Explainability

Each recommendation includes:

- Final decision
- Confidence score
- Risk factors
- Candidate strengths
- Candidate weaknesses
- Reason for recommendation

---

# Benefits

- Transparent hiring decisions
- Consistent evaluation
- Recruiter-friendly output
- Explainable AI recommendations