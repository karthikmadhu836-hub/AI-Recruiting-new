# Risk Flagging System Design

## Objective

Provide recruiters with clear integrity risk indicators based on browser activity, behavioral signals, and environmental observations during AI interviews.

---

# Risk Categories

| Integrity Score | Risk Level |
|-----------------|------------|
| 75–100 | Low Risk |
| 50–74 | Moderate Risk |
| Below 50 | High Risk |

---

# Real-Time Warning Rules

| Event | Warning |
|--------|---------|
| Tab switches > 2 | Please stay on the interview screen |
| Multiple voices detected | Ensure you are alone during the interview |
| Focus loss > 3 | Please focus on the interview |
| Frequent gaze deviation | Maintain attention on the interview |

---

# Flagging Rules

| Event | Flag |
|--------|------|
| Excessive tab switching | High Tab Switching |
| Browser focus loss | Screen Focus Loss |
| Multiple speakers | Multiple Voices Detected |
| Repeated gaze deviation | Frequent Gaze Deviation |

---

# Pattern Recognition

The system identifies combinations of events that may indicate potential malpractice.

Examples:

- Repeated tab switching → Possible use of external resources
- Continuous voice detection → Possible external assistance
- Gaze deviation with long pauses → Possible note consultation
- Focus loss with delayed responses → Possible multitasking

---

# Recruiter Dashboard Output

```json
{
    "candidate_id": "C4001",
    "integrity_score": 68,
    "risk_level": "Moderate Risk",
    "flags": [
        "High Tab Switching",
        "Frequent Gaze Deviation"
    ],
    "warnings": [
        "Please stay on the interview screen."
    ]
}
```

---

# Integration Flow

```
Interview Start
        │
        ▼
Browser Activity Monitoring
        │
        ▼
Audio Monitoring
        │
        ▼
Behavior Analysis
        │
        ▼
Signal Aggregation
        │
        ▼
Integrity Risk Calculation
        │
        ▼
Warning & Flag Generation
        │
        ▼
Recruiter Dashboard
```

---

# Ethical Guidelines

- Candidate consent required
- No facial recognition
- No screen recording
- Metadata-only analysis
- Transparent integrity scoring

---

# Benefits

- Reduces interview malpractice
- Supports fair hiring decisions
- Provides explainable recruiter insights
- Preserves candidate privacy

---

# Future Improvements

- AI-based anomaly detection
- Voice identity verification
- Adaptive behavioral learning
- Cross-platform monitoring