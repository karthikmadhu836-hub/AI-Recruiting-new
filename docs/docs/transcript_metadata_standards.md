# Transcript Metadata Standards – Zecpath AI

## Objective

The Transcript Metadata Standards define the structure, consistency, and traceability rules for storing and processing AI-based voice interview transcripts in the Zecpath ATS AI system.

The goal is to ensure:
- Structured transcript storage
- AI-ready processing
- Multi-language support
- Auditability and scalability

---

# 1. Core Metadata Fields

| Field Name | Description |
|------------|-------------|
| transcript_id | Unique transcript identifier |
| candidate_id | Unique candidate identifier |
| job_id | Associated job role ID |
| question_id | Screening question reference |
| question_text | Question asked during interview |
| answer_text | Candidate response text |
| confidence_score | Speech-to-text confidence score |
| start_time | Start timestamp of answer |
| end_time | End timestamp of answer |
| duration_seconds | Duration of response |
| language | Spoken language |
| overall_confidence | Average confidence of transcript |
| created_at | Transcript creation timestamp |

---

# 2. Metadata Design Principles

## Consistency
All transcripts must follow a standardized schema structure.

## Traceability
Every answer should map to:
- Candidate
- Job
- Question

## Auditability
System should store:
- Timestamps
- Confidence scores
- Processing history

## Scalability
Architecture should support:
- Multi-language interviews
- Multiple interview rounds
- Large-scale transcript storage

---

# 3. Transcript Structure Example

```json
{
  "transcript_id": "T123",
  "candidate_id": "C123",
  "job_id": "J101",
  "language": "en",
  "conversation": [
    {
      "question_id": "Q1",
      "question_text": "Can you introduce yourself?",
      "answer_text": "I am a backend developer.",
      "confidence_score": 0.94,
      "start_time": "00:00:02",
      "end_time": "00:00:10",
      "duration_seconds": 8
    }
  ],
  "overall_confidence": 0.92,
  "created_at": "2026-04-21T10:00:00Z"
}