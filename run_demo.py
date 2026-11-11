import json
import os

print("\n🚀 Running ATS Demo...\n")

os.system("python main_pipeline.py")

output_file = "data/outputs/final_pipeline_output.json"

if os.path.exists(output_file):

    with open(output_file) as f:
        data = json.load(f)

    print("\n🏆 TOP 5 CANDIDATES:\n")

    for i, item in enumerate(data[:5], 1):
        print(f"{i}. Resume: {item['resume']}")
        print(f"   JD: {item['jd']}")
        print(f"   Score: {item['score']}")
        print(f"   Eligibility: {item.get('eligibility', 'NOT ADDED')}")
        print("-" * 40)

else:
    print("❌ Output file not found")