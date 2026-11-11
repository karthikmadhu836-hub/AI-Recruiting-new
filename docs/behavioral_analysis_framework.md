# Behavioral Analysis Framework

## Objective

Convert observable behavioral signals into recruiter-friendly insights while maintaining privacy and fairness.

---

# Step 1 — Capture Signals

Input signals include:

- Eye focus
- Head stability
- Facial engagement
- Attention patterns

---

# Step 2 — Normalize Signals

Convert all raw values into a normalized range between **0 and 1**.

Example

| Raw Value | Normalized |
|-----------|-----------:|
| High | 1.0 |
| Medium | 0.5 |
| Low | 0.2 |

---

# Step 3 — Pattern Detection

Behavioral patterns detected:

- Focus
- Distraction
- Nervous gestures
- Engagement

---

# Step 4 — Weighted Scoring

| Signal | Weight |
|---------|-------:|
| Eye Focus | 30% |
| Head Stability | 20% |
| Engagement | 30% |
| Low Distraction | 20% |

Formula

```
Behavior Score =
Eye Focus × 0.30 +
Head Stability × 0.20 +
Engagement × 0.30 +
(1 − Distraction) × 0.20
```

---

# Step 5 — Generate Insights

The system produces:

- Behavior Score
- Focus Level
- Engagement Level
- Risk Level

Example

```json
{
    "behavior_score": 78.5,
    "focus_level": "High",
    "engagement": "Strong",
    "risk": "Low Risk"
}
```

---

# Behavioral Levels

| Score | Level |
|--------|-------|
| 85–100 | Highly Focused |
| 70–84 | Good Engagement |
| 50–69 | Moderate |
| Below 50 | Distracted |

---

# Ethical Guidelines

- No facial recognition
- No identity storage
- Metadata only
- Candidate consent required
- Transparent scoring
- Explainable outputs

---

# Benefits

- Improves interview evaluation
- Supports recruiter decisions
- Privacy preserving
- Easy integration

---

# Future Enhancements

- Gesture recognition
- Blink detection
- Posture analysis
- Real-time attention monitoring