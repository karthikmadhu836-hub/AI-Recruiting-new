# Edge Case & Failure Handling – Zecpath AI

## Objective

To ensure AI system stability under real-world unpredictable conditions.

---

# Edge Cases Covered

| Case | Handling Strategy |
|------|-------------------|
| Missing Answer | Retry / Skip |
| Poor Audio | Ask repeat |
| Background Noise | Clean text |
| Language Mixing | Offer language switch |
| Incomplete Answer | Ask follow-up |
| Unclear Answer | Simplify question |

---

# Error Handling Strategy

1. Detect issue
2. Trigger fallback
3. Retry with limit
4. Skip if unresolved

---

# Retry Policy

| Retry Count | Action |
|-------------|--------|
| 1st Attempt | Retry |
| 2nd Attempt | Simplify |
| 3rd Attempt | Skip |

---

# Safety Features

- Prevent infinite loops
- Graceful conversation exit
- User-friendly prompts

---

# Advantages

- Handles real-world noise
- Improves robustness
- Enhances candidate experience

---

# Limitations

- Rule-based detection
- Limited multilingual support

---

# Future Improvements

- ML-based noise detection
- Real-time language translation
- Context-aware fallback logic