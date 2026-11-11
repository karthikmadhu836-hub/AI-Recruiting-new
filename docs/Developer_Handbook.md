# HR Interview AI Developer Handbook – Zecpath

## Objective

This handbook provides integration guidance, scoring logic, troubleshooting instructions, and maintenance information for developers.

---

# Integration Workflow

## Step 1

Call Start Interview API

```http
POST /start
```

Receive:

* Session ID
* Initial Questions

---

## Step 2

Collect Candidate Responses

Supported Input:

* Voice
* Text

---

## Step 3

Submit Answers

```http
POST /answer
```

Receive:

* Follow-up Question
* Next Question

---

## Step 4

Continue Until Completion

Repeat answer submission until interview ends.

---

## Step 5

Generate Final Report

```http
GET /report/{session_id}
```

Receive:

* Final Score
* Hiring Recommendation
* Summary

---

# Scoring Logic

## HR Score Formula

HR Score =
(Relevance × Weight)

*

(Communication × Weight)

*

(Confidence × Weight)

*

(Consistency × Weight)

---

## Unified Score Formula

Final Score =
(ATS × 0.30)

*

(Screening × 0.30)

*

(HR × 0.40)

---

# Troubleshooting Guide

| Issue                       | Solution                |
| --------------------------- | ----------------------- |
| No response detected        | Retry STT               |
| Wrong intent classification | Improve intent keywords |
| Low score anomaly           | Verify normalization    |
| API timeout                 | Retry request           |
| Missing report              | Validate session ID     |

---

# Debug Checklist

* API logs verified
* Inputs validated
* Scores within expected range
* No missing fields
* Model outputs reviewed

---

# Maintenance Guidelines

Weekly:

* Review logs
* Validate scoring consistency

Monthly:

* Update question bank
* Re-test interview flows

Quarterly:

* Review fairness metrics
* Audit AI decisions

---

# Advantages

* Modular architecture
* Easy integration
* Recruiter-friendly outputs
* Scalable deployment

---

# Limitations

* Some rule-based components
* Requires backend infrastructure
* Limited real-time learning

---

# Future Roadmap

* AI SDK
* Real-Time Streaming APIs
* Adaptive Learning
* Advanced Explainability Dashboard

---

# Test Script

```python
def test_api_format():
    response = {
        "candidate_id": "C1",
        "final_score": 80
    }

    assert "candidate_id" in response
```
