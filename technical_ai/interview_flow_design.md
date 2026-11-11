# Zecpath Technical Interview Flow Design

## Objective

Define the complete interview flow for a role-based adaptive technical interview.

---

# Technical Interview Flow

```text
                 START
                    │
                    ▼
      Candidate Introduction
                    │
                    ▼
      Detect Experience Level
                    │
                    ▼
        Map Job Role & Skills
                    │
                    ▼
     Set Initial Difficulty Level
                    │
                    ▼
     Ask Conceptual Questions
                    │
                    ▼
        Evaluate Responses
                    │
         ┌──────────┴──────────┐
         │                     │
    Good Answer          Poor Answer
         │                     │
 Increase Difficulty    Reduce Difficulty
         │                     │
         └──────────┬──────────┘
                    ▼
      Ask Coding Problems
                    │
                    ▼
   Ask Scenario-Based Questions
                    │
                    ▼
 System Design (Experienced Candidates)
                    │
                    ▼
      Calculate Technical Score
                    │
                    ▼
 Generate Technical Report
                    │
                    ▼
                   END
```

---

# Interview States

| State | Description |
|--------|-------------|
| Start | Interview Initialized |
| Introduction | Candidate Introduction |
| Experience Detection | Years of Experience Classified |
| Skill Mapping | Role Skills Loaded |
| Question Generation | Technical Questions Generated |
| Answer Evaluation | AI Evaluates Candidate Answer |
| Difficulty Adjustment | Question Level Updated |
| Technical Scoring | Score Computed |
| Report Generation | Final Technical Report |
| Completed | Interview Finished |

---

# State Transitions

```text
START
   ↓
INTRODUCTION
   ↓
EXPERIENCE DETECTION
   ↓
ROLE MAPPING
   ↓
QUESTION GENERATION
   ↓
ANSWER EVALUATION
   ↓
DIFFICULTY ADJUSTMENT
   ↓
QUESTION GENERATION
        ↑
        │
 (Repeat until interview ends)
        │
        ▼
TECHNICAL SCORING
   ↓
REPORT GENERATION
   ↓
END
```

---

# Design Principles

- Adaptive questioning
- Progressive difficulty
- Role-specific evaluation
- Explainable scoring
- Modular architecture
- Scalable interview pipeline

---

# Future Enhancements

- Live coding interviews
- AI-generated coding problems
- LLM-based code review
- Real-time IDE integration
- Automatic plagiarism detection