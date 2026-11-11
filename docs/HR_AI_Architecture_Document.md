# Zecpath HR Interview AI – System Architecture

## Objective

This document describes the architecture of the HR Interview AI system, including core modules, data flow, and system interactions.

---

# High-Level Architecture

Frontend (Web / Mobile App)

↓

Backend API Layer

↓

HR Interview AI System

* Question Generator
* Conversation Engine
* Follow-Up Engine
* Answer Understanding Engine
* Communication Analyzer
* Confidence & Behavior Analyzer
* HR Scoring Engine
* Aptitude Engine
* Summary Generator

↓

Database / Storage

---

# Data Flow

User Input (Voice/Text)

↓

Speech-to-Text Processing

↓

Answer Processing

↓

AI Evaluation

* Intent Detection
* Communication Analysis
* Confidence Analysis
* Scoring

↓

Report Generation

↓

API Response

↓

Recruiter Dashboard

---

# Core Modules

| Module                 | Responsibility                         |
| ---------------------- | -------------------------------------- |
| Question Generator     | Generates interview questions          |
| Conversation Engine    | Manages interview flow                 |
| Follow-Up Engine       | Creates contextual follow-up questions |
| Answer Engine          | Extracts intent and meaning            |
| Communication Analyzer | Evaluates communication quality        |
| Confidence Analyzer    | Detects confidence signals             |
| HR Scoring Engine      | Calculates interview scores            |
| Summary Generator      | Creates recruiter-friendly reports     |

---

# Storage Layer

Candidate Data:

* Resume
* Interview Responses
* Scores
* Reports

Database Options:

* PostgreSQL
* MongoDB

---

# Technology Stack

Backend:

* Python
* Flask / FastAPI

AI Layer:

* NLP
* Rule-Based Models
* Machine Learning

Database:

* PostgreSQL
* MongoDB

---

# System Benefits

* Modular architecture
* Easy maintenance
* Scalable design
* Explainable AI decisions

---

# Future Improvements

* Real-time AI scoring
* Voice emotion analysis
* Multi-language support
* Streaming interview sessions
