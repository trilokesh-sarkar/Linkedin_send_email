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
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<style>

body {{
    margin: 0;
    padding: 20px;
    background: #f7f9fc;
    font-family: 'Segoe UI', Arial, sans-serif;
    color: #2d3748;
}}

.wrapper {{
    max-width: 760px;
    margin: auto;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
}}

.content {{
    padding: 40px;
}}

.content p {{
    font-size: 15px;
    line-height: 1.8;
    margin-bottom: 16px;
}}

.highlight-box {{
    background: #f8fafc;
    border-left: 4px solid #2563eb;
    padding: 20px;
    margin: 25px 0;
    border-radius: 6px;
}}

.highlight-box h3 {{
    margin-top: 0;
    color: #2563eb;
    font-size: 17px;
}}

.highlight-box ul {{
    margin: 0;
    padding-left: 20px;
}}

.highlight-box li {{
    margin-bottom: 12px;
    line-height: 1.7;
}}

.skills {{
    background: #eff6ff;
    border-radius: 6px;
    padding: 18px;
    margin-top: 20px;
    font-size: 14px;
}}

.skills-title {{
    font-weight: 600;
    margin-bottom: 8px;
}}

.signature {{
    margin-top: 35px;
    border-top: 1px solid #e2e8f0;
    padding-top: 25px;
}}

.signature-name {{
    font-size: 18px;
    font-weight: 600;
    color: #2563eb;
}}

.contact {{
    margin-top: 8px;
    color: #4a5568;
}}

.links {{
    margin-top: 15px;
}}

.links a {{
    text-decoration: none;
    color: #2563eb;
    margin-right: 16px;
    font-weight: 500;
}}

.footer {{
    text-align: center;
    background: #f8fafc;
    padding: 15px;
    font-size: 12px;
    color: #718096;
    border-top: 1px solid #e2e8f0;
}}

</style>

</head>

<body>

<div class="wrapper">

    <div class="content">

        <p>Dear {author},</p>

        <p>
            I hope you are doing well.
        </p>

        <p>
            I am writing to express my interest in the
            <strong>{role}</strong> position at
            <strong>{company}</strong>.
        </p>

        <p>
            I have over two years of professional experience working across
            Data Analytics, Data Engineering, Machine Learning, Generative AI,
            Big Data Processing and Business Intelligence projects.
            Throughout my career, I have delivered scalable solutions
            for Retail, Healthcare and BFSI domains while collaborating
            closely with cross-functional business and engineering teams.
        </p>

        <div class="highlight-box">

            <h3>Professional Highlights</h3>

            <ul>

                <li>
                    Built LLM-powered taxonomy audit pipelines using
                    GPT-4o, Apache Airflow, AWS, PostgreSQL and Redshift,
                    improving data quality and operational scalability.
                </li>

                <li>
                    Developed OCR and NLP automation solutions that reduced
                    manual effort by more than 80% while improving processing
                    accuracy.
                </li>

                <li>
                    Designed interactive dashboards and analytics solutions
                    using Power BI, SQL and Looker Studio to support
                    strategic business decision-making.
                </li>

                <li>
                    Implemented Machine Learning, Computer Vision and
                    Predictive Analytics solutions for real-world
                    business use cases.
                </li>

                <li>
                    Published research on adversarial robustness of
                    Generative AI systems
                    (arXiv:2404.04245).
                </li>

            </ul>

        </div>

        <div class="skills">

            <div class="skills-title">
                Technical Skills
            </div>

            Python • SQL • Power BI • AWS • Spark •
            Machine Learning • Deep Learning • NLP •
            Generative AI • Data Engineering • Data Analytics

        </div>

        <p>
            I have attached my resume for your review.
            I would welcome the opportunity to discuss how my
            technical expertise and experience align with the
            requirements of this position and how I can contribute
            to the continued success of {company}.
        </p>

        <p>
            Thank you for your time and consideration.
            I look forward to hearing from you and would be glad
            to discuss my qualifications in greater detail.
        </p>

        <div class="signature">

            <div class="signature-name">
                {your_name}
            </div>

            <div class="contact">
                📧 {your_email}<br>
                📱 {your_phone}
            </div>

            <div class="links">

                <a href="https://www.linkedin.com/in/trilokesh-sarkar/">
                    LinkedIn
                </a>

                <a href="https://github.com/trilokesh-sarkar">
                    GitHub
                </a>

                <a href="https://arxiv.org/abs/2404.04245">
                    Research Publication
                </a>

            </div>

        </div>

    </div>

    <div class="footer">
        Resume Attached
    </div>

</div>

</body>
</html>
"""

    return subject, html