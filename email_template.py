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

    subject = f"🚀 Application for {role} | Serving Notice Period | {your_name}"

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
I am a Generative AI and Agentic AI professional with <b>2 years of experience</b>
building LLM-powered automation and document-intelligence solutions. I am currently
serving my notice period and am actively exploring opportunities where I can contribute.
</p>

<p>
🚀 In my current role, I build LLM-powered automation solutions with the
following role-relevant strengths:
</p>

<ul>
  <li><b>Generative &amp; Agentic AI:</b> GPT-4o API integration, Prompt Engineering,
  LLM-driven workflow design, tool calling to external data sources, human-in-the-loop
  validation, automated error correction, LLM output evaluation, and
  resource-constrained fine-tuning.</li>
  <li><b>Document Intelligence:</b> OCR/NLP automation, Named Entity Recognition
  (NER), PyTesseract OCR, regex-based extraction, and document digitization.</li>
  <li><b>Workflow Delivery:</b> Python, AWS, Apache Airflow, Amazon Redshift,
  PostgreSQL, and Label Studio for scalable LLM-powered workflows.</li>
</ul>

<p>
I translate business requirements into reliable Generative AI workflows with
measurable results. Recent OCR/NLP automation reduced manual extraction effort
by <b>up to 80%</b>. My resume includes further project outcomes and technical
details relevant to <b>{role}</b>.
</p>

<p>
📎 I have attached my resume for your review and would welcome the opportunity
to have a brief conversation about how my Generative AI and agentic workflow
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

