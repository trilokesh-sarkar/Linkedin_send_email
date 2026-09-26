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
I am an AI/ML professional with <b>2 years of experience</b> building
LLM-powered and agentic AI workflows, OCR/NLP pipelines, and computer vision
solutions. I am currently serving my notice period and am actively exploring
opportunities where I can contribute.
</p>

<p>
🚀 In my current role, I build data-driven and AI-powered solutions involving
the following role-relevant strengths:
</p>

<ul>
  <li><b>AI/ML:</b> Machine Learning, Deep Learning, Computer Vision, image
  classification, model evaluation, and YOLOv8-based ANPR solutions.</li>
  <li><b>Generative &amp; Agentic AI:</b> GPT-4o API integration, Prompt Engineering,
  LLM-driven workflow design, tool calling, human-in-the-loop validation, LLM
  output evaluation, and resource-constrained fine-tuning.</li>
  <li><b>NLP &amp; Document AI:</b> Named Entity Recognition (NER), OCR/NLP
  automation, PyTesseract OCR, regex-based extraction, and document digitization.</li>
  <li><b>Data &amp; cloud:</b> Python, SQL, AWS, Amazon Redshift, PostgreSQL,
  Apache Airflow, ETL pipelines, Label Studio, and workflow automation.</li>
</ul>

<p>
I translate business requirements into reliable AI workflows with measurable
results. Recent work reduced manual extraction effort by <b>up to 80%</b>, while
marketing analytics dashboards improved engagement by <b>15%</b> and conversions
by <b>12%</b>. My resume includes further project outcomes and technical details
relevant to <b>{role}</b>.
</p>

<p>
📎 I have attached my resume for your review and would welcome the opportunity
to have a brief conversation about how my AI/ML and production engineering
experience can support the goals of <b>{company}</b>. Thank you for your
consideration.
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

