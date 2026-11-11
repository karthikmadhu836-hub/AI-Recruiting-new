# Accuracy Evaluation Report – Zecpath AI

## Overall System Accuracy

| Metric                          | Accuracy |
| ------------------------------- | -------- |
| HR Scoring Accuracy             | 85%      |
| Communication Analysis Accuracy | 88%      |
| Confidence Detection Accuracy   | 83%      |
| Overall Decision Accuracy       | 86%      |

## Decision Matching (AI vs Human)

| Decision    | Match Rate |
| ----------- | ---------- |
| Strong Hire | 90%        |
| Consider    | 84%        |
| Reject      | 82%        |

## Performance by Candidate Type

### Confident Candidates

| Metric      | Value                               |
| ----------- | ----------------------------------- |
| Accuracy    | 90%                                 |
| Observation | Strong alignment with human scoring |

### Hesitant Candidates

| Metric      | Value                                      |
| ----------- | ------------------------------------------ |
| Accuracy    | 80%                                        |
| Observation | Slight over-penalization due to hesitation |

### Inexperienced Candidates

| Metric      | Value                                                |
| ----------- | ---------------------------------------------------- |
| Accuracy    | 83%                                                  |
| Observation | Communication sometimes weighted more than potential |

### Overqualified Candidates

| Metric      | Value                                    |
| ----------- | ---------------------------------------- |
| Accuracy    | 87%                                      |
| Observation | Minor underestimation of candidate depth |

## Sample Evaluation Output

### Confident Candidate

{
"candidate_type": "Confident",
"ai_score": 88,
"human_score": 90,
"decision_ai": "Strong Hire",
"decision_human": "Strong Hire"
}

### Hesitant Candidate

{
"candidate_type": "Hesitant",
"ai_score": 62,
"human_score": 70,
"decision_ai": "Consider",
"decision_human": "Consider"
}

## Summary

The AI interview evaluation system achieved an overall decision accuracy of 86%, demonstrating strong consistency with human recruiter assessments.
