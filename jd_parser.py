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

    Examples:
        jobs@capgemini.com            -> Capgemini
        careers@amazon.jobs           -> Amazon
        recruiter@subdomain.tcs.com   -> TCS
        hiring@mail.microsoft.com     -> Microsoft
        hr@accentureindia.com         -> Accenture
        abc@gmail.com                 -> None
    """

    if not email or "@" not in email:
        return None

    try:
        domain = email.split("@")[1].strip().lower()

        # Remove port if present
        domain = domain.split(":")[0]

        parts = domain.split(".")

        # Common email/service subdomains
        skip_domains = {
            "mail",
            "email",
            "mailer",
            "smtp",
            "mx",
            "careers",
            "career",
            "jobs",
            "job",
            "recruitment",
            "recruiting",
            "talent",
            "hr",
            "hiring",
            "apply",
            "team",
            "people",
        }

        # Check all domain parts from right to left
        candidates = []

        if len(parts) >= 2:
            candidates.append(parts[-2])

        candidates.extend(reversed(parts[:-2]))

        for candidate in candidates:

            candidate = re.sub(
                r"[^a-z0-9]",
                "",
                candidate.lower()
            )

            if not candidate:
                continue

            if candidate in GENERIC_EMAIL_DOMAINS:
                continue

            if candidate in skip_domains:
                continue

            # Explicit canonical mapping
            if candidate in COMPANY_CANONICAL:
                return COMPANY_CANONICAL[candidate]

            # Common aliases
            aliases = {
                "amazonaws": "Amazon AWS",
                "aws": "Amazon AWS",
                "tataconsultancyservices": "TCS",
                "tcs": "TCS",
                "accentureindia": "Accenture",
                "microsoft": "Microsoft",
                "google": "Google",
                "meta": "Meta",
                "facebook": "Meta",
                "ibm": "IBM",
                "ey": "EY",
                "kpmg": "KPMG",
                "pwc": "PwC",
                "deloitte": "Deloitte",
                "capgemini": "Capgemini",
                "infosys": "Infosys",
                "wipro": "Wipro",
                "cognizant": "Cognizant",
                "hcl": "HCL",
                "techmahindra": "Tech Mahindra",
                "oracle": "Oracle",
                "sap": "SAP",
                "adobe": "Adobe",
                "salesforce": "Salesforce",
                "servicenow": "ServiceNow",
                "zoho": "Zoho",
            }

            if candidate in aliases:
                return aliases[candidate]

            # Remove common suffixes
            cleaned = re.sub(
                r"(india|global|group|tech|technologies|solutions|services)$",
                "",
                candidate
            )

            if cleaned and len(cleaned) > 2:
                return cleaned.title()

        return None

    except Exception:
        return None


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

def extract_company_from_text(text):
    """
    Extract company directly from hiring post text.
    """

    patterns = [

        # Gartner is expanding...
        r"\b([A-Z][A-Za-z& ]{2,50})\s+is\s+(?:hiring|looking|expanding|growing|seeking)",

        # Join Gartner
        r"(?:join|joining)\s+([A-Z][A-Za-z& ]{2,50})",

        # Hiring at Gartner
        r"hiring\s+(?:at\s+)?([A-Z][A-Za-z& ]{2,50})",

        # Gartner team
        r"\b([A-Z][A-Za-z& ]{2,50})\s+(?:team|group|center|centre|coe)\b",
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            company = match.group(1).strip()

            company = re.sub(
                r"\s+",
                " ",
                company
            )

            if len(company) > 2:
                return company

    return None


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

        local_part = (
            result["recruiter_email"]
            .split("@")[0]
        )

        name_parts = re.split(
            r"[._\-]",
            local_part
        )

        if name_parts:

            first_name = (
                name_parts[0]
                .strip()
                .capitalize()
            )

            # Skip generic recruiter aliases
            recruiter_blacklist = {
                "hr",
                "jobs",
                "career",
                "careers",
                "recruitment",
                "recruiter",
                "hiring",
                "talent",
                "team",
                "admin",
                "support",
                "info",
            }

            if (
                first_name.isalpha()
                and len(first_name) > 2
                and first_name.lower()
                not in recruiter_blacklist
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

            result["experience"] = (
                match.group(1)
            )

            break

    if result["experience"]:

        normalized = normalize_exp(
            result["experience"]
        )

        rng = exp_range(normalized)

        if rng:

            result["experience_category"] = (
                exp_category(
                    rng[0],
                    rng[1]
                )
            )

    # --------------------------------------------------
    # Company Extraction
    # --------------------------------------------------

    company_patterns = [

        # Gartner is expanding...
        r"\b([A-Z][A-Za-z& ]{2,50})\s+is\s+(?:hiring|looking|expanding|growing|seeking)",

        # Infosys is hiring...
        r"\b([A-Z][A-Za-z& ]{2,50})\s+is\s+hiring",

        # Join Gartner
        r"(?:join|joining)\s+([A-Z][A-Za-z& ]{2,50})",

        # Hiring at Gartner
        r"hiring\s+(?:at\s+)?([A-Z][A-Za-z& ]{2,50})",

        # Company: Gartner
        r"company\s*[:\-]\s*(.+)",

        # Organization: Gartner
        r"organization\s*[:\-]\s*(.+)",

        # Employer: Gartner
        r"employer\s*[:\-]\s*(.+)",

        # at Gartner
        r"at\s+([A-Z][A-Za-z0-9\s&]+?)(?:\s*[,.\n])",

        # for Gartner
        r"for\s+([A-Z][A-Za-z0-9\s&]+?)(?:\s*[,.\n])",
    ]

    blacklist = {
        "we",
        "our",
        "team",
        "community",
        "linkedin",
        "hello linkedin community",
    }

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

            company_value = re.sub(
                r"\s+",
                " ",
                company_value
            )

            if (
                company_value.lower()
                not in blacklist
                and len(company_value) < 60
            ):
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