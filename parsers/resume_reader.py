import os
import re
from pdfminer.high_level import extract_text
import docx
from utils.logger import get_logger

logger = get_logger()

# -------- PDF Reader --------
def read_pdf(file_path):
    try:
        text = extract_text(file_path)
        logger.info(f"PDF read successfully: {file_path}")
        return text
    except Exception as e:
        logger.error(f"Error reading PDF: {e}")
        return ""

# -------- DOCX Reader --------
def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        logger.info(f"DOCX read successfully: {file_path}")
        return text
    except Exception as e:
        logger.error(f"Error reading DOCX: {e}")
        return ""

# -------- Cleaner --------
def clean_text(text):
    text = text.lower()  # normalize case
    text = re.sub(r'\n+', '\n', text)  # remove extra newlines
    text = re.sub(r'[^a-zA-Z0-9\s\n]', '', text)  # remove symbols
    text = re.sub(r'\s+', ' ', text)  # normalize spaces
    return text.strip()

# -------- Main Extractor --------
def extract_resume(file_path):
    if file_path.endswith(".pdf"):
        raw_text = read_pdf(file_path)
    elif file_path.endswith(".docx"):
        raw_text = read_docx(file_path)
    else:
        logger.error("Unsupported file format")
        return ""

    cleaned_text = clean_text(raw_text)
    return cleaned_text