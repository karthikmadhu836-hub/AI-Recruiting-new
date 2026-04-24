import os
import json
from parsers.jd_parser import parse_jd

INPUT_DIR = "data/job_descriptions"
OUTPUT_DIR = "data/processed_jd"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_all_jds():
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".txt"):
            file_path = os.path.join(INPUT_DIR, file)
            
            jd_data = parse_jd(file_path)
            
            output_file = os.path.join(OUTPUT_DIR, file.replace(".txt", ".json"))
            
            with open(output_file, "w") as f:
                json.dump(jd_data, f, indent=4)

if __name__ == "__main__":
    process_all_jds()