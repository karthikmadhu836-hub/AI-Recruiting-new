# ATS API Specification

## Base URL

http://localhost:8000

---

## 1. Upload Resume

**Endpoint:** POST /upload_resume
**Description:** Upload candidate resume

**Request:**

* File (PDF/DOCX)

**Response:**
{
"message": "Resume uploaded successfully",
"file_name": "resume1.pdf"
}

---

## 2. Parse Resume

**Endpoint:** POST /parse_resume

**Request:**
{
"file_name": "resume1.pdf"
}

**Response:**
{
"text": "Extracted resume text..."
}

---

## 3. Score Candidate

**Endpoint:** POST /score

**Request:**
{
"resume_file": "resume1.pdf",
"jd_file": "jd1.txt"
}

**Response:**
{
"score": 0.82,
"details": {}
}

---

## 4. Shortlist Candidates

**Endpoint:** POST /shortlist

**Request:**
{
"jd_file": "jd1.txt"
}

**Response:**
{
"shortlisted": [],
"review": [],
"rejected": []
}
