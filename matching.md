## 📊 Day 12: Semantic Matching Engine

### Objective

To measure semantic similarity between resumes and job descriptions.

---

### Approach

* Convert text into TF-IDF vectors
* Compute cosine similarity between resume and JD
* Generate similarity score

---

### Features

* Captures contextual similarity
* Works beyond keyword matching
* Lightweight and fast

---

### Accuracy

* Similar roles: 75–90%
* Different domains: 50–70%

---

### Limitations

* Not as powerful as deep learning models
* Sensitive to text quality

---

### Improvements

* Use Sentence Transformers (BERT)
* Fine-tune embeddings
* Add domain-specific training data
