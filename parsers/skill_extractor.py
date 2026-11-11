import re
from collections import defaultdict

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
    "php":["php"],
    "go":["golang","go"],
    "rust":["rust"],
    "r":[" r "],
    "matlab":["matlab"],

    # Database
    "sql":["sql"],
    "mysql":["mysql"],
    "postgresql":["postgresql","postgres"],
    "mongodb":["mongodb"],
    "oracle":["oracle"],
    "sqlite":["sqlite"],

    # Data Science
    "machine learning":["machine learning","ml"],
    "deep learning":["deep learning"],
    "artificial intelligence":["artificial intelligence","ai"],
    "data analysis":["data analysis"],
    "data visualization":["data visualization"],
    "statistics":["statistics"],
    "power bi":["power bi"],
    "tableau":["tableau"],
    "excel":["excel","microsoft excel"],
    "numpy":["numpy"],
    "pandas":["pandas"],
    "scikit learn":["scikit","sklearn"],
    "tensorflow":["tensorflow"],
    "keras":["keras"],
    "pytorch":["pytorch"],

    # Cloud
    "aws":["aws","amazon web services"],
    "azure":["azure"],
    "gcp":["google cloud","gcp"],

    # DevOps
    "docker":["docker"],
    "kubernetes":["kubernetes"],
    "jenkins":["jenkins"],
    "git":["git"],
    "github":["github"],
    "linux":["linux"],

    # Web
    "html":["html"],
    "css":["css"],
    "react":["react"],
    "angular":["angular"],
    "vue":["vue"],
    "nodejs":["node","nodejs"],
    "django":["django"],
    "flask":["flask"],
    "fastapi":["fastapi"],

    # Quality Control / QA
    "quality control":["quality control","qc"],
    "quality assurance":["quality assurance","qa"],
    "inspection":["inspection"],
    "testing":["testing"],
    "manual testing":["manual testing"],
    "automation testing":["automation testing"],
    "selenium":["selenium"],
    "junit":["junit"],
    "testng":["testng"],
    "root cause analysis":["root cause analysis","rca"],
    "capa":["capa","corrective action"],
    "gmp":["gmp"],
    "glp":["glp"],
    "iso 9001":["iso 9001"],
    "documentation":["documentation"],
    "compliance":["compliance"],
    "auditing":["audit","auditing"],
    "risk management":["risk management"],
    "process improvement":["process improvement"],
    "lean":["lean"],
    "six sigma":["six sigma"],
    "spc":["spc"],
    "calibration":["calibration"],

    # Business Analyst
    "business analysis":["business analysis"],
    "requirement gathering":["requirement gathering"],
    "agile":["agile"],
    "scrum":["scrum"],
    "jira":["jira"],
    "user stories":["user stories"],

    # HR
    "recruitment":["recruitment"],
    "talent acquisition":["talent acquisition"],
    "screening":["screening"],
    "interviewing":["interviewing"],

    # Finance
    "accounting":["accounting"],
    "financial analysis":["financial analysis"],
    "taxation":["taxation"],

    # Soft Skills
    "communication":["communication"],
    "leadership":["leadership"],
    "teamwork":["team player","teamwork"],
    "problem solving":["problem solving"],
    "critical thinking":["critical thinking"],
    "analytical skills":["analytical","analytical skills"],
    "attention to detail":["attention to detail","detail oriented"],
    "time management":["time management"]
}


# --------------------------------------------------
# CLEAN TEXT
# --------------------------------------------------

def clean_text(text):

    if text is None:
        return ""

    text = text.lower()
    text = re.sub(r'[^a-z0-9+#\.\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text


# --------------------------------------------------
# SKILL EXTRACTION
# --------------------------------------------------

def extract_skills(text):

    text = clean_text(text)

    found = defaultdict(int)

    for skill, variants in SKILL_DB.items():

        for variant in variants:

            pattern = rf"\b{re.escape(variant)}\b"

            matches = re.findall(pattern, text)

            if matches:
                found[skill] += len(matches)

    skills = sorted(found.keys())

    confidence = {}

    for skill, count in found.items():

        confidence[skill] = round(min(1.0, count/3),2)

    return skills, confidence

