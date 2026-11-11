# Machine Test AI Framework – Zecpath

## Objective

Design an AI-driven system that evaluates real-world technical skills through practical machine tests such as coding, debugging, file-based assignments, and system design exercises.

---

# Supported Machine Test Types

| Test Type | Description |
|-----------|-------------|
| Coding Problems | Algorithm and logic-based programming tasks |
| Debugging Tasks | Identify and fix bugs in existing code |
| File-Based Tasks | Modify or complete project files |
| Mini System Design | Design scalable software components |

---

# High-Level Architecture

```
Candidate Interface (IDE/Web Editor)
            │
            ▼
     Code Capture Engine
            │
            ▼
 Execution Sandbox Engine
            │
            ▼
   Test Case Evaluation
            │
            ▼
 Code Quality Analyzer
            │
            ▼
 Time & Attempt Tracker
            │
            ▼
 Machine Test Scoring Engine
            │
            ▼
 Technical Report Generator
```

---

# Workflow

1. Candidate starts the machine test.
2. Candidate writes or modifies code.
3. System captures code snapshots.
4. Code executes inside a secure sandbox.
5. Test cases are evaluated.
6. Runtime and execution statistics are collected.
7. Code quality is analyzed.
8. Time taken and attempts are recorded.
9. Final score is calculated.
10. Technical report is generated.

---

# Evaluation Parameters

- Correctness
- Runtime Efficiency
- Code Quality
- Problem Solving Ability
- Completion Time

---

# Advantages

- Practical technical assessment
- Objective evaluation
- Automated scoring
- Scalable architecture

---

# Limitations

- Rule-based code quality evaluation
- Limited optimization detection
- No plagiarism detection

---

# Future Improvements

- AI-powered code review
- Plagiarism detection
- Live collaborative coding
- LLM-assisted evaluation