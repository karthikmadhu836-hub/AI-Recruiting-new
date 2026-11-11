import re

# --------------------------------------------------
# MASTER SKILL DATABASE
# --------------------------------------------------

SKILL_DB = {

    # Programming
    "python":["python"],
    "java":["java"],
    "c":["c"],
    "c++":["c++","cpp"],
    "c#":["c#"],
    "javascript":["javascript","js"],
    "typescript":["typescript"],

    # Database
    "sql":["sql"],
    "mysql":["mysql"],
    "postgresql":["postgresql","postgres"],
    "mongodb":["mongodb"],

    # AI
    "machine learning":["machine learning","ml"],
    "deep learning":["deep learning"],
    "artificial intelligence":["artificial intelligence","ai"],
    "data analysis":["data analysis"],
    "statistics":["statistics"],
    "excel":["excel","microsoft excel"],
    "power bi":["power bi"],
    "tableau":["tableau"],

    # Cloud
    "aws":["aws"],
    "azure":["azure"],
    "gcp":["google cloud","gcp"],

    # QA / QC
    "quality control":["quality control","qc"],
    "quality assurance":["quality assurance","qa"],
    "quality management":["quality management"],
    "inspection":["inspection"],
    "testing":["testing"],
    "sampling":["sampling"],
    "root cause analysis":["root cause analysis","rca"],
    "corrective action":["corrective action","capa"],
    "preventive action":["preventive action"],
    "iso 9001":["iso 9001"],
    "gmp":["gmp"],
    "glp":["glp"],
    "documentation":["documentation"],
    "compliance":["compliance"],
    "auditing":["audit","auditing"],
    "risk management":["risk management"],
    "analytical skills":["analytical","analytical skills"],
    "attention to detail":["attention to detail"],
    "communication":["communication"],
    "teamwork":["team player","teamwork"],
    "process improvement":["process improvement"],
    "six sigma":["six sigma"],
    "lean":["lean"],
    "spc":["spc"],

    # Business
    "business analysis":["business analysis"],
    "agile":["agile"],
    "scrum":["scrum"],
    "jira":["jira"]
}

# --------------------------------------------------
# ROLE DATABASE
# --------------------------------------------------

ROLE_DB = [

    "quality control analyst",
    "quality analyst",
    "quality assurance analyst",
    "quality engineer",
    "quality control engineer",

    "data analyst",
    "business analyst",

    "software engineer",
    "software developer",
    "backend developer",
    "frontend developer",
    "full stack developer",

    "machine learning engineer",
    "data scientist",

    "project manager",
    "manager",
    "consultant",
    "intern"
]

# --------------------------------------------------
# CLEAN TEXT
# --------------------------------------------------

def clean_text(text):

    if not text:
        return ""

    text = text.lower()

    text = re.sub(r'[^a-z0-9+#.,/\-\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# --------------------------------------------------
# SKILL EXTRACTION
# --------------------------------------------------

def extract_skills(text):

    skills=[]

    for skill,variants in SKILL_DB.items():

        for variant in variants:

            pattern=rf"\b{re.escape(variant)}\b"

            if re.search(pattern,text):

                skills.append(skill)

                break

    return sorted(list(set(skills)))

# --------------------------------------------------
# JOB TITLE
# --------------------------------------------------

def extract_role(text):

    for role in ROLE_DB:

        if role in text:

            return role

    return "unknown"

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

def extract_experience(text):

    matches=re.findall(

        r'(\d+)\+?\s*(?:years|year|yrs|yr)',

        text

    )

    if matches:

        return max([int(x) for x in matches])

    return 0

# --------------------------------------------------
# EDUCATION
# --------------------------------------------------

def extract_education(text):

    education=[]

    mapping={

        "phd":"PhD",

        "doctorate":"PhD",

        "m.tech":"M.Tech",

        "mtech":"M.Tech",

        "b.tech":"B.Tech",

        "btech":"B.Tech",

        "mba":"MBA",

        "mca":"MCA",

        "bca":"BCA",

        "msc":"M.Sc",

        "bsc":"B.Sc",

        "be":"B.E"

    }

    for key,value in mapping.items():

        if key in text:

            education.append(value)

    return list(set(education))

# --------------------------------------------------
# CERTIFICATIONS
# --------------------------------------------------

def extract_certifications(text):

    certs=[]

    possible=[

        "six sigma",

        "iso 9001",

        "aws",

        "azure",

        "gcp",

        "pmp",

        "scrum master"

    ]

    for cert in possible:

        if cert in text:

            certs.append(cert)

    return certs

# --------------------------------------------------
# LOCATION
# --------------------------------------------------

def extract_location(text):

    match=re.search(

        r'location\s*[:\-]\s*([a-zA-Z ]+)',

        text

    )

    if match:

        return match.group(1).strip()

    return "Not Specified"

# --------------------------------------------------
# EMPLOYMENT TYPE
# --------------------------------------------------

def extract_employment_type(text):

    types=[

        "full time",

        "part time",

        "contract",

        "internship",

        "temporary",

        "remote",

        "hybrid"

    ]

    for t in types:

        if t in text:

            return t

    return "Not Specified"

# --------------------------------------------------
# MAIN PARSER
# --------------------------------------------------

def parse_job_description(jd_text):

    cleaned=clean_text(jd_text)

    return{

        "job_title":extract_role(cleaned),

        "required_skills":extract_skills(cleaned),

        "min_experience_years":extract_experience(cleaned),

        "education_required":extract_education(cleaned),

        "certifications":extract_certifications(cleaned),

        "employment_type":extract_employment_type(cleaned),

        "location":extract_location(cleaned),

        "job_description_text":jd_text,

        "cleaned_text":cleaned
    }

