# Zecpath HR Interview AI – API Specification

## Base URL

https://api.zecpath.ai/v1/hr-interview

---

# 1. Start Interview

## Endpoint

POST /start

### Request

```json
{
  "candidate_id": "C101",
  "job_id": "J501",
  "role_type": "technical",
  "experience_level": "fresher"
}
```

### Response

```json
{
  "session_id": "S123",
  "questions": [
    "Tell me about yourself",
    "What are your strengths?"
  ]
}
```

---

# 2. Submit Answer

## Endpoint

POST /answer

### Request

```json
{
  "session_id": "S123",
  "question_id": "Q1",
  "answer": "I have experience in Python...",
  "duration": 6
}
```

### Response

```json
{
  "follow_up": "Can you elaborate more?",
  "next_question": "Describe your teamwork experience"
}
```

---

# 3. Get Final Report

## Endpoint

GET /report/{session_id}

### Response

```json
{
  "candidate_id": "C101",
  "final_score": 78,
  "decision": "Strong Hire",
  "summary": {
    "strengths": ["Good communication"],
    "weaknesses": ["Minor hesitation"]
  }
}
```

---

# Error Response Format

```json
{
  "error_code": "INVALID_INPUT",
  "message": "Missing candidate_id",
  "status": 400
}
```

---

# Data Models

## Answer Object

```json
{
  "question_id": "Q1",
  "answer_text": "I worked on backend systems",
  "intent": "experience",
  "skills": ["Python"],
  "confidence_score": 80,
  "communication_score": 75
}
```

## Report Object

```json
{
  "candidate_id": "C101",
  "scores": {
    "ats": 75,
    "screening": 70,
    "hr": 80
  },
  "final_score": 77,
  "decision": "Hire"
}
```

---

# Security Guidelines

* HTTPS only
* JWT Authentication
* Rate Limiting
* Encrypted Data Storage
* Audit Logging

---

# Future API Enhancements

* GraphQL Support
* WebSocket Streaming
* Real-Time Interview Sessions
* SDK Support
