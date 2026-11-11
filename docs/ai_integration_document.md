# Zecpath AI Integration Architecture

## Objective

Define how all AI modules integrate with backend services, databases, and external systems in a secure, scalable, and production-ready architecture.

---

# System Architecture

Frontend (Web / Mobile)

↓

Backend API (Node.js / Django)

↓

AI Microservices Layer

- Resume Parser API
- ATS Scoring API
- Screening AI API
- HR Interview API
- Technical Interview API
- Machine Test API
- Decision AI API
- Report Generator API

↓

Database

- Candidate Profiles
- Interview Scores
- Reports
- Audit Logs

↓

Object Storage

- Resumes
- Interview Recordings
- Reports

---

# Backend → AI → Database Flow

1. Candidate uploads resume.
2. Backend stores the resume.
3. Resume Parser extracts structured information.
4. ATS Engine calculates ATS score.
5. Screening AI evaluates screening responses.
6. HR Interview AI conducts HR interview.
7. Technical AI evaluates technical interview.
8. Machine Test AI evaluates coding task.
9. Aggregation Engine combines all scores.
10. Decision AI generates final recommendation.
11. Hiring Report Generator creates recruiter report.
12. Backend stores results and sends them to the frontend.

---

# Integration Principles

- REST APIs
- JSON communication
- Stateless AI services
- Microservice architecture
- Independent deployment
- Scalable processing

---

# Security

- JWT Authentication
- OAuth2 (Third-party integrations)
- HTTPS
- Role-Based Access Control
- API Rate Limiting
- Request Validation

---

# Processing Strategy

## Asynchronous APIs

- Resume Parsing
- ATS Scoring
- Report Generation

Queue → Worker → Database → Callback

## Synchronous APIs

- Live Interview Scoring
- Real-Time Feedback
- Decision Engine

Request → AI → Immediate Response

---

# Future Improvements

- GraphQL Gateway
- Kafka Event Streaming
- gRPC Internal Communication
- Kubernetes Deployment