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
    line-height: 1.7;
    color: #333333;
">

<p>Dear {author},</p>

<p>
I am writing to express my interest in the
<b style="color:#0F4C81;">{role}</b> position at
<b style="color:#0F4C81;">{company}</b>.
I currently work as a Data Analyst with experience in
<b>Python, SQL, Data Analytics, Machine Learning, Data Science,
Generative AI, Large Language Models (LLMs), NLP, Power BI,
AWS, PostgreSQL, Redshift, and Apache Airflow</b>.
</p>

<p>
In my current role, I build data-driven solutions involving
<b>ETL Pipelines, Data Engineering, Business Intelligence,
Forecasting, Automation, Information Extraction, OCR,
Machine Learning, Generative AI, Prompt Engineering,
Embeddings, Vector Search, Semantic Search,
Knowledge Retrieval, and Retrieval-Augmented Generation (RAG)</b>.
I have worked on scalable analytics and AI solutions that improve
operational efficiency, data quality, and business decision-making.
</p>

<p>
I have attached my resume for your review and would welcome the
opportunity to discuss how my experience in
<b style="color:#0F4C81;">
Data Science, Machine Learning, Generative AI, LLM Applications,
RAG Systems, Data Engineering, Cloud Technologies,
Analytics, and Business Intelligence
</b>
can contribute to your team.
Thank you for your time and consideration, and I look forward to hearing from you.
</p>

<p>
Kind Regards,<br><br>

<b>{your_name}</b><br>
📧 {your_email}<br>
📱 {your_phone}<br><br>

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