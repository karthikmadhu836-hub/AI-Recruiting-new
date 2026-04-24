import os

folder_path = r"data/raw/resumes"   # your resumes folder

files = sorted(os.listdir(folder_path))

counter = 1

for file in files:
    if file.endswith(".pdf") or file.endswith(".docx"):
        
        ext = file.split(".")[-1]  # keep original extension
        
        new_name = f"sample_resume_{counter}.{ext}"
        
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        
        counter += 1

print("All files renamed successfully!")