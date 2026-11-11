# AI Integrity & Malpractice Detection Framework – Zecpath

## Objective

Design a privacy-preserving AI framework that detects potential malpractice or external assistance during technical and HR interviews using non-invasive behavioral and system signals.

---

# Core Signals Monitored

| Signal | Description |
|---------|-------------|
| Tab Switching | Detects frequent switching away from the interview tab |
| Screen Focus Loss | Browser visibility changes or window minimization |
| External Voice | Detects multiple speakers during the interview |
| Gaze Deviation | Repeated looking away from the screen |
| Idle Behavior | Long pauses without user interaction |

---

# High-Level Architecture

```
Browser Activity Tracker
        │
        ▼
Focus Detection Module
        │
        ▼
Audio Analyzer
        │
        ▼
Behavioral AI
        │
        ▼
Signal Aggregator
        │
        ▼
Integrity Risk Engine
        │
        ▼
Warning & Flagging System
        │
        ▼
Recruiter Dashboard
```

---

# Detection Strategy

## Browser Activity

- Count tab switches
- Detect browser focus changes
- Monitor idle duration

---

## Audio Monitoring

- Detect multiple speakers
- Detect continuous background conversation

---

## Behavioral Monitoring

- Eye movement stability
- Gaze deviation
- Attention consistency

---

# Design Principles

- No identity recognition
- No keystroke logging
- No screen recording
- Metadata-only processing
- Candidate consent required

---

# Advantages

- Fair interview monitoring
- Non-invasive detection
- Recruiter-friendly reports
- Explainable integrity scoring

---

# Limitations

- Browser permission dependency
- Possible false positives
- Requires webcam and microphone access

---

# Future Improvements

- AI anomaly detection
- Voice identity verification
- Adaptive cheating detection
- Cross-device monitoring