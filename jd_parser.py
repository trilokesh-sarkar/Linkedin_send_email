"""
Enhanced Rule-based Job Description Parser.
Extracts role, company, recruiter name, recruiter email,
location, experience, and experience category.

No AI/LLM used.
"""

import re

GENERIC_EMAIL_DOMAINS = {
    "gmail",
    "yahoo",
    "outlook",
    "hotmail",
    "live",
    "aol",
    "protonmail",
    "icloud",
    "zoho",
    "mail",
    "gmx",
    "yopmail",
    "rediff",
    "msn",
}

CITY_CANONICAL = {
    "bangalore": "Bangalore",
    "bengaluru": "Bangalore",
    "bangaluru": "Bangalore",
    "bangalure": "Bangalore",
    "banglore": "Bangalore",
    "bengluru": "Bangalore",
    "bengalore": "Bangalore",
    "bombay": "Mumbai",
    "madras": "Chennai",
    "calcutta": "Kolkata",
    "poona": "Pune",
    "new delhi": "Delhi",
}

COMPANY_CANONICAL = {
    "tcs": "Tata Consultancy Services",
    "infosys": "Infosys",
    "wipro": "Wipro",
    "capgemini": "Capgemini",
    "cts": "Cognizant",
    "cognizant": "Cognizant",
    "accenture": "Accenture",
    "ibm": "IBM",
    "deloitte": "Deloitte",
    "ey": "Ernst & Young",
    "pwc": "PwC",
    "kpmg": "KPMG",
    "oracle": "Oracle",
    "google": "Google",
    "amazon": "Amazon",
}

EXP_PATTERNS = [
    r"(\d+\s*-\s*\d+\s*years?)",
    r"(\d+\s*to\s*\d+\s*years?)",
    r"(\d+\+?\s*years?)",
    r"(minimum\s*\d+\s*years?)",
    r"(up to\s*\d+\s*years?)",
]

TARGET_ROLES = [
    "Data Scientist",
    "Data Analyst",
    "Business Analyst",
    "Data Engineer",
    "Machine Learning Engineer",
    "ML Engineer",
    "AI Engineer",
    "AI/ML Engineer",
    "Generative AI Engineer",
    "GenAI Engineer",
    "LLM Engineer",
    "NLP Engineer",
    "Computer Vision Engineer",
    "Analytics Engineer",
    "BI Analyst",
    "Python Developer",
]


def detect_target_role(text: str) -> str:
    text_lower = text.lower()

    # Exact role match
    for role in TARGET_ROLES:
        if role.lower() in text_lower:
            return role

    role_keywords = {
        "Data Scientist": [
            "data scientist",
            "datascientist",
        ],
        "Data Analyst": [
            "data analyst",
            "analytics analyst",
            "mis analyst",
        ],
        "Business Analyst": [
            "business analyst",
        ],
        "Data Engineer": [
            "data engineer",
            "etl engineer",
            "big data engineer",
        ],
        "Machine Learning Engineer": [
            "machine learning engineer",
            "ml engineer",
        ],
        "AI Engineer": [
            "ai engineer",
            "artificial intelligence engineer",
        ],
        "AI/ML Engineer": [
            "ai/ml",
            "ai ml",
            "ai-ml",
        ],
        "Generative AI Engineer": [
            "generative ai",
            "gen ai",
            "genai",
        ],
        "LLM Engineer": [
            "llm engineer",
            "large language model",
        ],
        "NLP Engineer": [
            "nlp engineer",
            "natural language processing",
        ],
        "Computer Vision Engineer": [
            "computer vision",
            "cv engineer",
        ],
        "Analytics Engineer": [
            "analytics engineer",
        ],
        "BI Analyst": [
            "bi analyst",
            "business intelligence analyst",
            "power bi analyst",
        ],
        "Python Developer": [
            "python developer",
        ],
    }

    for role, keywords in role_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                return role

    return ""


def extract_company_from_email(email):
    """
    Extract company name from recruiter email.
    Example:
        jobs@capgemini.com -> Capgemini
    """
    if not email or "@" not in email:
        return None

    domain = email.split("@")[1].lower()
    domain = domain.split(".")[0]

    if domain in GENERIC_EMAIL_DOMAINS:
        return None

    return COMPANY_CANONICAL.get(domain, domain.title())


def normalize_exp(exp):
    """
    Normalize experience string.
    Example:
        '2 to 4 years' -> '2 - 4'
    """
    return (
        exp.replace("years", "")
        .replace("year", "")
        .replace("yrs", "")
        .replace("minimum", "")
        .replace("up to", "")
        .replace("to", "-")
        .strip()
    )


def exp_range(exp):
    """
    Convert experience text into numeric range.
    """
    nums = re.findall(r"\d+", exp)

    if len(nums) == 1:
        return int(nums[0]), int(nums[0])

    if len(nums) >= 2:
        return int(nums[0]), int(nums[1])

    return None


def exp_category(low, high):
    """
    Categorize experience level.
    """
    if low <= 1 and high <= 1:
        return "0–1 years (Fresher)"

    if low <= 1 and high <= 3:
        return "1–3 years (Junior)"

    if low <= 2 and high <= 5:
        return "2–5 years (Mid-Level)"

    if low >= 5:
        return "5+ years (Senior)"

    return f"{low}-{high} years"


def clean_location(location):
    """
    Normalize city names.
    """
    location = re.sub(
        r"(location|based in|work location|city|:)",
        "",
        location,
        flags=re.IGNORECASE,
    ).strip()

    return CITY_CANONICAL.get(
        location.lower(),
        location.title()
    )


def extract_job_details(jd_text: str) -> dict:
    """
    Parse Job Description and extract structured details.
    """

    result = {
        "role": "",
        "company": "",
        "recruiter_name": "",
        "recruiter_email": "",
        "location": "",
        "experience": "",
        "experience_category": "",
    }

    # --------------------------------------------------
    # Email Extraction
    # --------------------------------------------------
    email_pattern = r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"

    emails = re.findall(email_pattern, jd_text)

    if emails:
        result["recruiter_email"] = emails[0]

    # --------------------------------------------------
    # Recruiter Name Extraction
    # --------------------------------------------------
    if result["recruiter_email"]:
        local_part = result["recruiter_email"].split("@")[0]

        name_parts = re.split(
            r"[._\-]",
            local_part
        )

        if name_parts:
            first_name = name_parts[0].capitalize()

            if (
                first_name.isalpha()
                and len(first_name) > 2
            ):
                result["recruiter_name"] = first_name
    # --------------------------------------------------
    # Role Extraction
    # --------------------------------------------------

    role = detect_target_role(jd_text)

    if role:
        result["role"] = role

    else:

        role_patterns = [
            r"designation\s*[:\-]\s*([^\n]+)",
            r"role\s*[:\-]\s*([^\n]+)",
            r"position\s*[:\-]\s*([^\n]+)",
            r"job\s*title\s*[:\-]\s*([^\n]+)",
            r"hiring\s+for\s+([^\n,.]+)",
            r"opening\s+for\s+([^\n,.]+)",
            r"looking\s+for\s+([^\n,.]+)",
            r"we\s+are\s+hiring\s+([^\n,.]+)",
            r"we\s+are\s+looking\s+for\s+([^\n,.]+)",
            r"immediate\s+opening\s+for\s+([^\n,.]+)",
        ]

        for pattern in role_patterns:

            match = re.search(
                pattern,
                jd_text,
                re.IGNORECASE,
            )

            if match:

                role = match.group(1).strip()

                role = re.sub(
                    r"\s+(at|in|for)\s+.*$",
                    "",
                    role,
                    flags=re.IGNORECASE,
                )

                result["role"] = role
                break
    # --------------------------------------------------
    # Location Extraction
    # --------------------------------------------------
    location_patterns = [
        r"location\s*[:\-]\s*(.+)",
        r"based\s*in\s*[:\-]?\s*(.+)",
        r"work\s*location\s*[:\-]\s*(.+)",
        r"city\s*[:\-]\s*(.+)",
    ]

    for pattern in location_patterns:
        match = re.search(
            pattern,
            jd_text,
            re.IGNORECASE,
        )

        if match:
            location_value = (
                match.group(1)
                .split("\n")[0]
                .strip()
            )

            result["location"] = clean_location(
                location_value
            )
            break

    # --------------------------------------------------
    # Experience Extraction
    # --------------------------------------------------
    for pattern in EXP_PATTERNS:
        match = re.search(
            pattern,
            jd_text,
            re.IGNORECASE,
        )

        if match:
            result["experience"] = match.group(1)
            break

    if result["experience"]:
        normalized = normalize_exp(
            result["experience"]
        )

        rng = exp_range(normalized)

        if rng:
            result["experience_category"] = exp_category(
                rng[0],
                rng[1]
            )

    # --------------------------------------------------
    # Company Extraction
    # --------------------------------------------------
    company_patterns = [
        r"company\s*[:\-]\s*(.+)",
        r"organization\s*[:\-]\s*(.+)",
        r"employer\s*[:\-]\s*(.+)",
        r"at\s+([A-Z][A-Za-z0-9\s&]+?)(?:\s*[,.\n])",
        r"for\s+([A-Z][A-Za-z0-9\s&]+?)(?:\s*[,.\n])",
    ]

    for pattern in company_patterns:
        match = re.search(
            pattern,
            jd_text,
            re.IGNORECASE,
        )

        if match:
            company_value = (
                match.group(1)
                .strip()
                .rstrip(".")
            )

            if len(company_value) < 60:
                result["company"] = company_value
                break

    # --------------------------------------------------
    # Company from Email Fallback
    # --------------------------------------------------
    if (
        not result["company"]
        and result["recruiter_email"]
    ):
        result["company"] = (
            extract_company_from_email(
                result["recruiter_email"]
            )
            or ""
        )

    return result