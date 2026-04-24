DEVELOPER GUIDE – ATS SYSTEM

1. PROJECT STRUCTURE

- main_pipeline.py → Main execution file
- parsers/ → Resume parsing
- ats_engine/ → Similarity logic
- scoring/ → Scoring system
- utils/ → Normalization and fairness
- data/ → Input and output files

2. HOW TO RUN

Step 1: Open terminal
Step 2: Navigate to project folder
Step 3: Activate virtual environment
Step 4: Run:
    python main_pipeline.py

3. INPUT REQUIREMENTS

- Resumes must be placed in:
  data/raw/resumes/

- Job descriptions must be placed in:
  data/raw/job_descriptions/

4. OUTPUT

- Results saved in:
  data/outputs/final_pipeline_output.json

5. ADDING NEW JDs

- Add new .txt files to job_descriptions folder

6. ADDING NEW RESUMES

- Add PDF/DOCX files to resumes folder

7. TROUBLESHOOTING

Problem: File not found
Solution: Check folder paths

Problem: Empty output
Solution: Check input files

Problem: Parsing error
Solution: Ensure valid PDF/DOCX format

8. EXTENDING SYSTEM

- Add ML model for training
- Improve entity detection
- Integrate with frontend API