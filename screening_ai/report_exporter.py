def export_report_text(report):

    text = f"""
Candidate ID: {report['candidate_id']}
Job ID: {report['job_id']}
Final Score: {report['final_score']}
Decision: {report['decision']}

--- Strengths ---
{chr(10).join(report['summary']['strengths'])}

--- Risks ---
{chr(10).join(report['summary']['risks'])}

--- Missing Data ---
{chr(10).join(report['summary']['missing_data'])}

--- Highlights ---
Salary: {report['highlights']['salary_expectation']}
Availability: {report['highlights']['availability']}
Skills: {', '.join(report['highlights']['confirmed_skills'])}
"""

    return text