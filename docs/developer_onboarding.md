# Developer Onboarding Guide

## Welcome

Welcome to the Zecpath AI Hiring Platform.

This guide helps developers set up the project and understand the overall architecture.

---

# Prerequisites

- Python 3.10+
- Git
- VS Code
- Docker (Optional)
- PostgreSQL

---

# Project Setup

## Clone Repository

```bash
git clone <repository_url>
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests

```bash
pytest
```

---

## Start Application

```bash
python app.py
```

---

# Project Structure

```
Ai-Recruiting-New/

ai_core/
api/
behavior_ai/
integrity_ai/
machine_test/
parsers/
screening_ai/
observability/
tests/
docs/
utils/
```

---

# Development Workflow

1. Create feature branch

2. Implement feature

3. Write unit tests

4. Verify all tests

5. Create Pull Request

6. Code Review

7. Merge

---

# Coding Standards

- Follow PEP-8
- Use type hints where applicable
- Keep modules independent
- Add logging
- Write tests

---

# Testing

Run all tests

```bash
pytest
```

Run specific test

```bash
python -m tests.test_resume_parser
```

---

# Logging

Use centralized logging.

Never use print statements inside production modules.

---

# Documentation

Update documentation whenever:

- API changes
- Architecture changes
- New AI module added
- Database changes

---

# Troubleshooting

## Import Errors

Check virtual environment.

Verify PYTHONPATH.

---

## Module Not Found

Ensure __init__.py exists.

---

## API Errors

Check logs.

Validate request payload.

---

## Performance Issues

Check cache.

Monitor response times.

---

# Best Practices

- Modular Design
- Reusable Functions
- Proper Exception Handling
- Unit Testing
- Documentation
- Code Reviews

---

# Contribution Guidelines

Every new module should include:

- Source Code
- Tests
- Documentation
- Example Usage

---

# Contacts

Project Name

**Zecpath AI Hiring Platform**

Version

**v1.0**