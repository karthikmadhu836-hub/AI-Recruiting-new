# Speech-to-Text Accuracy Report – Zecpath AI

## Objective

To evaluate speech-to-text accuracy across different accents,
noise levels, and speaking styles.

---

# Test Dataset Summary

| Test Type | Samples |
|------------|----------|
| Clean Audio | 20 |
| Noisy Background | 20 |
| Indian Accent | 20 |
| Mixed Accent | 20 |
| Fast Speech | 10 |
| Interrupted Speech | 10 |
| Total | 100 |

---

# Accuracy Results

| Condition | Accuracy |
|------------|-----------|
| Clean Audio | 96% |
| Indian Accent | 91% |
| Mixed Accent | 88% |
| Noisy Background | 82% |
| Fast Speech | 85% |
| Interrupted Speech | 80% |

---

# Overall Accuracy

Average Accuracy = 87%

---

# Error Types

| Error Type | Example |
|------------|----------|
| Misheard words | "node" → "note" |
| Missing punctuation | No sentence breaks |
| Filler noise | "um", "uh" |
| Broken sentences | Partial phrases |

---

# Improvements Applied

- Filler word removal
- Punctuation correction
- Silence detection
- Text normalization

---

# Sample Input

um i have uh 3 years experience in python and django

# Sample Output

I have 3 years experience in python and django.

---

# Future Improvements

- Real-time streaming STT
- Accent adaptation models
- Context-aware punctuation