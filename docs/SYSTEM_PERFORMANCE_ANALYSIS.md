# System Performance Analysis

## Objective

Evaluate execution speed, throughput, and consistency of the complete AI hiring pipeline.

---

# Processing Time

| Stage | Average Time |
|--------|-------------|
| ATS | 0.5 sec |
| Screening | 1.2 sec |
| HR Interview | 1.5 sec |
| Technical Interview | 1.8 sec |
| Full Pipeline | 5.5 sec |

---

# Throughput

- Approximately 100 candidates/hour
- Supports batch processing
- Modular architecture allows horizontal scaling

---

# Identified Inconsistencies

| Issue | Impact |
|--------|--------|
| High Technical + Low HR | Mixed hiring decisions |
| Strong ATS + Weak Machine Test | Candidate overestimation |
| Behavioral mismatch | Decision uncertainty |
| Short answers | False negatives |

---

# Performance Summary

## Strengths

- Fast ATS processing
- Stable technical evaluation
- Consistent machine test scoring
- Modular architecture

## Weaknesses

- HR and behavioral alignment requires improvement
- Rule-based thresholds
- Simulated evaluation dataset

---

# Final Assessment

Overall system performance is stable with acceptable response times and high decision consistency for production-ready evaluation.