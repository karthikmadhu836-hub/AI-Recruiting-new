import os

folder = "data/job_descriptions"
os.makedirs(folder, exist_ok=True)

for i in range(1, 66):
    file_path = os.path.join(folder, f"jd{i}.txt")
    
    with open(file_path, "w") as f:
        f.write(f"Sample Job Description {i}\n\nSkills: Python, SQL\nExperience: 2 years")

print("66 JD files created successfully!")