ATS TECHNICAL DOCUMENTATION

1. INTRODUCTION
The ATS (Applicant Tracking System) is designed to automate resume screening by comparing candidate resumes with job descriptions. It evaluates, scores, and ranks candidates efficiently.

2. SYSTEM OVERVIEW
Input:
- Resumes (PDF/DOCX)
- Job Descriptions (TXT)

Output:
- Candidate scores
- Ranked candidate list
- Shortlisted candidates

3. SYSTEM COMPONENTS

a) Resume Parser
- Extracts text from PDF and DOCX files

b) Text Preprocessing
- Normalization
- Noise removal
- Personal information masking

c) Semantic Matching Engine
- Calculates similarity between resume and JD

d) Entity Detection
- Extracts skills and keywords
- Improves matching accuracy

e) Scoring Engine
- Combines:
  • Skill score
  • Experience score
  • Education score
  • Semantic similarity

f) Ranking Engine
- Sorts candidates based on score

g) Evaluation Module
- Calculates precision and recall

4. OPTIMIZATION TECHNIQUES

- Resume caching (avoids re-reading files)
- Similarity caching (avoids recomputation)
- Efficient loop structure

5. FAIRNESS IMPROVEMENTS

- Mask personal information
- Normalize text data
- Reduce bias in scoring

6. SCALABILITY

- Supports 65+ job descriptions
- Handles 100+ resumes
- Efficient for large datasets

7. LIMITATIONS

- Not a trained ML model
- Depends on text quality
- Limited entity extraction

8. FUTURE IMPROVEMENTS

- Add ML model training
- Use advanced NLP models
- Improve entity recognition