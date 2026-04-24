# ATS Integration Flow

## Overview

This document describes how backend systems interact with the ATS AI.

---

## Flow Steps

1. Resume Upload
   Client uploads resume via API

2. Resume Parsing
   Backend extracts structured text

3. Job Description Parsing
   JD is processed into structured format

4. Scoring
   AI compares resume and JD

5. Shortlisting
   Candidates are filtered into categories

6. Output
   Results returned as JSON

---

## Async Handling

* Resume processing can be queued
* Scoring can run in background jobs
* Results stored in database

---

## Error Handling

* Invalid file format → 400 error
* Missing file → 404 error
* Server failure → 500 error

---

## Logging

* Each request logged
* Errors tracked
* Scores stored for auditing
