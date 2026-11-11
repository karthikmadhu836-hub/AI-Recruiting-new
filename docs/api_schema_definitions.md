# API Request & Response Schemas

---

## Resume Parser API

### Request

```json
{
  "candidate_id": "C100",
  "file_url": "resume.pdf"
}
```

### Response

```json
{
  "candidate_id": "C100",
  "skills": [
    "Python",
    "SQL"
  ],
  "experience": 2
}
```

---

## ATS Scoring API

### Request

```json
{
  "candidate_profile": {},
  "job_description": {}
}
```

### Response

```json
{
  "ats_score": 82,
  "matched_skills": [
    "Python",
    "SQL"
  ]
}
```

---

## Screening API

### Request

```json
{
  "candidate_id": "C100",
  "answers": []
}
```

### Response

```json
{
  "screening_score": 76,
  "transcript": []
}
```

---

## HR Interview API

### Request

```json
{
  "session_id": "HR001",
  "answers": []
}
```

### Response

```json
{
  "hr_score": 81,
  "summary": {}
}
```

---

## Technical Interview API

### Request

```json
{
  "session_id": "TECH001",
  "answers": []
}
```

### Response

```json
{
  "technical_score": 85,
  "feedback": {}
}
```

---

## Machine Test API

### Request

```json
{
  "candidate_id": "C100",
  "submission": {}
}
```

### Response

```json
{
  "machine_test_score": 79
}
```

---

## Decision API

### Request

```json
{
  "scores": {},
  "risk_flags": {}
}
```

### Response

```json
{
  "decision": "Selected",
  "confidence": 91
}
```