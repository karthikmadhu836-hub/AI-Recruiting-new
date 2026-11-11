# Machine Test Scoring Model – Zecpath

## Objective

Provide a structured scoring model for evaluating practical software engineering skills through machine tests.

---

# Evaluation Metrics

| Metric | Weight |
|---------|-------:|
| Correctness | 40% |
| Runtime Efficiency | 20% |
| Code Quality | 20% |
| Problem Solving | 20% |

---

# Final Score Formula

## Task Score

```
Task Score =
(Correctness × 0.40) +
(Efficiency × 0.20) +
(Code Quality × 0.20) +
(Problem Solving × 0.20)
```

---

## Overall Machine Test Score

```
Final Score =
(Task Score × 0.80) +
(Time Score × 0.20)
```

---

# Time-Based Scoring

| Time Used | Score |
|-----------|------:|
| ≤ 50% of limit | 100 |
| 50–100% | 70 |
| Above limit | 40 |

---

# Performance Levels

| Score | Result |
|-------:|--------|
| 85–100 | Excellent |
| 70–84 | Good Performance |
| 50–69 | Average |
| Below 50 | Needs Improvement |

---

# Example Output

```json
{
  "candidate_id": "C5001",
  "task_score": 78.5,
  "time_score": 70,
  "final_score": 76.8,
  "decision": "Good Performance"
}
```

---

# Benefits

- Objective evaluation
- Automated scoring
- Practical skill assessment
- Recruiter-friendly reports

---

# Limitations

- Rule-based code quality analysis
- No plagiarism detection
- Limited optimization analysis

---

# Future Improvements

- AI-powered code review
- AST-based analysis
- Code similarity detection
- Live coding evaluation