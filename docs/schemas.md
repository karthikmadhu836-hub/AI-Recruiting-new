# Input / Output Schemas

## Resume Upload

Input:
File (PDF/DOCX)

Output:
{
"file_name": "resume1.pdf"
}

---

## Resume Parsing

Input:
{
"file_name": "resume1.pdf"
}

Output:
{
"text": "string"
}

---

## Scoring

Input:
{
"resume_file": "resume1.pdf",
"jd_file": "jd1.txt"
}

Output:
{
"score": 0.82,
"bias_flags": [],
"details": {
"skills": 0.7,
"semantic": 0.85
}
}

---

## Shortlisting

Input:
{
"jd_file": "jd1.txt"
}

Output:
{
"shortlisted": [],
"review": [],
"rejected": []
}
