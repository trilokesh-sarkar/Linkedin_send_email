# email_template.py

from html import escape


def generate_email_content(
    author: str,
    company: str,
    role: str,
    your_name: str,
    your_email: str,
    your_phone: str,
):
    """
    Returns:
        subject, html_body
    """

    author = escape(author or "Hiring Team")
    company = escape(company or "your organization")
    role = escape(role or "Data Analyst")
    your_name = escape(your_name)
    your_email = escape(your_email)
    your_phone = escape(your_phone)

    # --------------------------------------------------
    # Professional Subject Line
    # --------------------------------------------------

    subject = f"🚀 Application for {role} | {your_name}"

    # --------------------------------------------------
    # Professional HTML Email
    # --------------------------------------------------

    html = f"""
    <html>
    <body style="
        font-family: Calibri, Arial, sans-serif;
        font-size: 14px;
        line-height: 1.8;
        color: #333333;
        max-width: 750px;
        margin: 0;
    ">

    <p>Dear {author},</p>

    <p>
    I hope you are doing well.
    </p>

    <p>
    I am writing to express my interest in the
    <b style="color:#0F4C81;">{role}</b>
    position at
    <b style="color:#0F4C81;">{company}</b>.
    </p>

    <p>
    I am currently working as a <b>Data Analyst</b> with experience across
    <b>Data Science, Machine Learning, Generative AI, Large Language Models (LLMs),
    Retrieval-Augmented Generation (RAG), NLP, Data Analytics, Data Engineering,
    Business Intelligence, and Cloud-based Data Platforms</b>.
    </p>

    <p>
    In my current role, I work closely with business and technical stakeholders
    to design and deliver scalable data and AI solutions. My experience includes
    building automated data pipelines, developing analytics dashboards, creating
    forecasting solutions, performing large-scale data analysis, and implementing
    machine learning workflows using modern cloud and data technologies.
    </p>

    <p>
    I have worked extensively with
    <b style="color:#0F4C81;">
    Python, SQL, PostgreSQL, Redshift, AWS, Apache Airflow,
    Power BI, ETL Pipelines, Data Warehousing, Data Modeling,
    Statistical Analysis, Predictive Analytics, Machine Learning,
    Deep Learning, NLP, OCR, Information Extraction,
    and Business Intelligence solutions.
    </b>
    </p>

    <p>
    Additionally, I have experience working on AI-focused projects involving
    <b style="color:#0F4C81;">
    Generative AI, Prompt Engineering, LLM Evaluation,
    RAG Pipelines, Vector Databases, Embedding Models,
    Semantic Search, Knowledge Retrieval, Entity Resolution,
    Taxonomy Classification, AI-powered Automation,
    Document Intelligence, and Retrieval Systems.
    </b>
    </p>

    <p>
    My technical toolkit includes
    <b>
    Python, SQL, Pandas, NumPy, Scikit-Learn, TensorFlow,
    XGBoost, Machine Learning, Deep Learning, NLP,
    LLMs, RAG, Prompt Engineering, Vector Search,
    Embeddings, AWS, PostgreSQL, Redshift,
    Apache Airflow, Power BI, Data Engineering,
    Data Analytics, Forecasting, Automation,
    Business Intelligence, and Cloud Computing.
    </b>
    </p>

    <p>
    I am particularly interested in opportunities where I can leverage
    Data Science, AI, Machine Learning, Generative AI, and advanced analytics
    to solve complex business problems and deliver measurable impact.
    </p>

    <p>
    I have attached my resume for your review and would welcome the opportunity
    to discuss how my experience, technical expertise, and problem-solving skills
    can contribute to the success of your team.
    </p>

    <p>
    Thank you for your time and consideration.
    I look forward to hearing from you.
    </p>

    <br>

    <p>
    Kind Regards,
    </p>

    <p>
    <b>{your_name}</b><br>
    📧 {your_email}<br>
    📱 {your_phone}
    </p>

    <p>
    <a href="https://www.linkedin.com/in/trilokesh-sarkar/">
    LinkedIn Profile
    </a>
    &nbsp; | &nbsp;
    <a href="https://github.com/trilokesh-sarkar">
    GitHub
    </a>
    </p>

    </body>
    </html>
    """  
    
    
    return subject, html