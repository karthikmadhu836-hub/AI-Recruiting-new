import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_extractor import extract_resume
from parsers.save_output import save_text

def test_resume_extraction():
    data_folder = "data"
    
    # Find any resume file (PDF or DOCX)
    file_path = None
    for file in os.listdir(data_folder):
        if file.endswith(".pdf") or file.endswith(".docx"):
            file_path = os.path.join(data_folder, file)
            break

    assert file_path is not None, "No resume file found in data/ folder"

    text = extract_resume(file_path)

    assert len(text) > 0, "Extracted text is empty"

    save_text("output_resume", text)