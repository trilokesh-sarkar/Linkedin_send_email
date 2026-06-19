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

    # ------------------------------------------
    # Subject
    # ------------------------------------------

    subject = f"🚀 Application for {role} | {your_name}"

    # ------------------------------------------
    # HTML Email
    # ------------------------------------------

    html = f"""
<html style="background-color:#FFFFFF;">
<body style="
    background-color:#FFFFFF;
    font-family:Calibri, Arial, sans-serif;
    font-size:14px;
    line-height:1.7;
    color:#333333;
    margin:0;
    padding:20px;
">

<p>Dear {author},</p>

<p>
📌 I am writing to express my interest in the
<b style="color:#0F4C81;">{role}</b> opportunity at
<b style="color:#0F4C81;">{company}</b>.
With experience in <b>Python, SQL, Data Analytics, Machine Learning,
Generative AI, LLMs, RAG, NLP, AWS, PostgreSQL, Redshift, Power BI,
and Apache Airflow</b>, I am excited about the opportunity to contribute
to the innovative work being done at <b>{company}</b>.
</p>

<p>
🚀 In my current role, I build data-driven and AI-powered solutions involving
<b>Data Science, Data Engineering, ETL Pipelines, Forecasting, Automation,
Prompt Engineering, Vector Search, Embeddings, Semantic Search,
Knowledge Retrieval, and Retrieval-Augmented Generation (RAG)</b>.
I enjoy solving complex business problems through data and AI while delivering
scalable solutions that create measurable business impact.
</p>

<p>
📎 I have attached my resume for your review and would welcome the opportunity
to discuss how my skills and experience can contribute to the continued success
of <b>{company}</b>. Thank you for your time and consideration, and I look
forward to hearing from you.
</p>

<p>
Best Regards,<br><br>

<b>{your_name}</b><br>

📧 <a href="mailto:{your_email}" style="color:#0F4C81;text-decoration:none;">
{your_email}
</a><br>

📱 {your_phone}<br>

🔗 <a href="https://www.linkedin.com/in/trilokesh-sarkar/"
style="color:#0F4C81;text-decoration:none;">
LinkedIn Profile
</a>

&nbsp; | &nbsp;

💻 <a href="https://github.com/trilokesh-sarkar"
style="color:#0F4C81;text-decoration:none;">
GitHub
</a>

</p>

</body>
</html>
"""


  
  
  
    return subject, html

