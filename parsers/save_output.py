import os
from utils.logger import get_logger

logger = get_logger()

OUTPUT_DIR = "data/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_text(filename, text):
    file_path = os.path.join(OUTPUT_DIR, filename + ".txt")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    logger.info(f"Saved cleaned resume: {file_path}")