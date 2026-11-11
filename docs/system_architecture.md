# Zecpath AI System Architecture

# High-Level Architecture

Frontend

↓

Backend APIs

↓

AI Services

↓

Database

↓

Storage

---

# AI Services

- Resume Parser
- ATS Engine
- Screening AI
- HR AI
- Technical AI
- Machine Test AI
- Behavioral AI
- Integrity AI
- Aggregation Engine
- Decision Engine
- Report Generator

---

# Data Flow

Candidate Upload

↓

Resume Parsing

↓

ATS Matching

↓

Screening

↓

HR Interview

↓

Technical Interview

↓

Machine Test

↓

Behavior Analysis

↓

Aggregation

↓

Decision

↓

Hiring Report

---

# Component Responsibilities

## Resume Parser

Extracts structured information from resumes.

## ATS Engine

Calculates resume-job matching score.

## Screening AI

Evaluates candidate responses.

## HR AI

Measures communication and HR competencies.

## Technical AI

Evaluates technical knowledge.

## Machine Test AI

Evaluates coding and practical tasks.

## Behavioral AI

Detects engagement and behavioral signals.

## Integrity AI

Detects cheating or suspicious behavior.

## Aggregation Engine

Combines all stage scores.

## Decision AI

Generates final hiring recommendation.

## Report Generator

Creates recruiter-friendly hiring reports.

---

# Database Objects

- Candidate
- Resume
- Job Description
- Interview Session
- Scores
- Reports
- Audit Logs

---

# API Flow

Frontend

↓

Backend

↓

AI APIs

↓

Database

↓

Frontend Response

---

# Deployment Architecture

Client

↓

NGINX

↓

Backend APIs

↓

AI Services

↓

Redis Cache

↓

PostgreSQL

↓

Monitoring

---

# Scalability

- Microservices
- Horizontal Scaling
- Load Balancer
- Docker Containers
- Kubernetes

---

# Monitoring

- Logging
- Metrics
- Alerts
- Tracing
- Audit Logs