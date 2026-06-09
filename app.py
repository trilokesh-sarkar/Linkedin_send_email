import os
import re
import smtplib
import streamlit as st

from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from jd_parser import extract_job_details
from email_template import generate_email_content
from db import init_db, save_application, get_all_applications

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()


def get_secret(key: str, default: str = "") -> str:
    """
    Get secret from Streamlit Cloud or local .env
    """
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key, default)


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Job Application Sender",
    layout="wide"
)

st.title("📧 Automated Job Application System")

# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

init_db()

# --------------------------------------------------
# Sidebar - User Information
# --------------------------------------------------

st.sidebar.header("👤 Your Details")

your_name = st.sidebar.text_input(
    "Full Name",
    value="Trilokesh Ranjan Sarkar"
)

your_email = st.sidebar.text_input(
    "Your Email",
    value="trilokesh086@gmail.com"
)

your_phone = st.sidebar.text_input(
    "Phone Number",
    value="8910384107"
)

# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

st.sidebar.header("📎 Resume Upload")

resume_file = st.sidebar.file_uploader(
    "Upload Resume (.pdf or .docx)",
    type=["pdf", "docx"]
)

if resume_file:
    st.sidebar.success(
        f"Uploaded: {resume_file.name}"
    )

# --------------------------------------------------
# SMTP Credentials
# --------------------------------------------------

st.sidebar.header("🔐 SMTP Credentials")

smtp_email = st.sidebar.text_input(
    "Sender Email (Gmail)",
    value=get_secret("SMTP_EMAIL")
)

smtp_password = st.sidebar.text_input(
    "App Password",
    value=get_secret("SMTP_PASSWORD"),
    type="password"
)

# --------------------------------------------------
# Main Tabs
# --------------------------------------------------

tab1, tab2 = st.tabs(
    ["📝 Apply", "📊 Application Tracker"]
)

# ==================================================
# APPLY TAB
# ==================================================

with tab1:

    st.subheader("Step 1: Paste Job Description")

    jd_text = st.text_area(
        "Paste the job description / hiring post here:",
        height=250,
        placeholder=(
            "Designation: Data Scientist\n"
            "Experience: 2-4 Years\n"
            "Location: Bangalore\n"
            "Send your resume to: recruiter@company.com"
        ),
    )

    # ----------------------------------------------
    # Extract Information
    # ----------------------------------------------

    if st.button("🔍 Extract Information"):

        if jd_text.strip():

            extracted = extract_job_details(jd_text)

            st.session_state["extracted"] = extracted

            st.success(
                "✅ Information extracted successfully!"
            )

            filled_fields = sum(
                bool(v)
                for v in extracted.values()
            )

            st.info(
                f"Detected {filled_fields}/{len(extracted)} fields."
            )

        else:
            st.warning(
                "Please paste a job description first."
            )

    # ----------------------------------------------
    # Display Extracted Data
    # ----------------------------------------------

    if "extracted" in st.session_state:

        extracted = st.session_state["extracted"]

        st.subheader(
            "Step 2: Review & Edit Extracted Details"
        )

        col1, col2 = st.columns(2)

        with col1:

            role = st.text_input(
                "Role / Designation",
                value=extracted.get(
                    "role",
                    ""
                )
            )

            company = st.text_input(
                "Company",
                value=extracted.get(
                    "company",
                    ""
                )
            )

            recruiter_name = st.text_input(
                "Recruiter Name",
                value=extracted.get(
                    "recruiter_name",
                    ""
                )
            )

        with col2:

            recruiter_email = st.text_input(
                "Recipient Email",
                value=extracted.get(
                    "recruiter_email",
                    ""
                )
            )

            location = st.text_input(
                "Location",
                value=extracted.get(
                    "location",
                    ""
                )
            )

            experience = st.text_input(
                "Experience",
                value=extracted.get(
                    "experience",
                    ""
                )
            )

            experience_category = st.text_input(
                "Experience Category",
                value=extracted.get(
                    "experience_category",
                    ""
                ),
                disabled=True
            )

        # ------------------------------------------
        # Job Insights
        # ------------------------------------------

        st.subheader("📈 Job Insights")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Company",
                company if company else "Unknown"
            )

        with c2:
            st.metric(
                "Location",
                location if location else "Unknown"
            )

        with c3:
            st.metric(
                "Experience",
                experience_category
                if experience_category
                else experience
            )

        # ------------------------------------------
        # Email Preview
        # ------------------------------------------

        st.subheader(
            "Step 3: Email Preview"
        )

        author = (
            recruiter_name
            if recruiter_name
            else "Hiring Team"
        )

        company_name = (
            company
            if company
            else "your organization"
        )

        if your_name and your_email:

            subject, email_html = generate_email_content(
                author=author,
                company=company_name,
                role=role,
                your_name=your_name,
                your_email=your_email,
                your_phone=your_phone,
            )

            st.components.v1.html(
                email_html,
                height=700,
                scrolling=True
            )

            # --------------------------------------
            # Send Email
            # --------------------------------------

            st.subheader(
                "Step 4: Send Application"
            )

            if st.button(
                "🚀 Send Email"
            ):

                email_regex = (
                    r"^[A-Za-z0-9._%+-]+"
                    r"@[A-Za-z0-9.-]+"
                    r"\.[A-Za-z]{2,}$"
                )

                if not recruiter_email:

                    st.error(
                        "Recipient email is required."
                    )

                elif not re.match(
                    email_regex,
                    recruiter_email
                ):

                    st.error(
                        "Invalid recruiter email address."
                    )

                elif not smtp_email:

                    st.error(
                        "Please provide sender email."
                    )

                elif not smtp_password:

                    st.error(
                        "Please provide Gmail App Password."
                    )

                elif not resume_file:

                    st.error(
                        "Please upload your resume."
                    )

                elif not your_name or not your_email:

                    st.error(
                        "Please complete your profile details."
                    )

                else:

                    try:

                        msg = MIMEMultipart()

                        msg["From"] = smtp_email
                        msg["To"] = recruiter_email

                        msg["Subject"] =  subject

                        # HTML Email Body
                        msg.attach(
                            MIMEText(
                                email_html,
                                "html"
                            )
                        )

                        # Resume Attachment
                        resume_bytes = resume_file.getvalue()

                        part = MIMEBase(
                            "application",
                            "octet-stream"
                        )

                        part.set_payload(
                            resume_bytes
                        )

                        encoders.encode_base64(
                            part
                        )

                        part.add_header(
                            "Content-Disposition",
                            f"attachment; filename={resume_file.name}",
                        )

                        msg.attach(part)

                        # Gmail SMTP
                        with smtplib.SMTP(
                            "smtp.gmail.com",
                            587
                        ) as server:

                            server.starttls()

                            server.login(
                                smtp_email,
                                smtp_password
                            )

                            server.sendmail(
                                smtp_email,
                                recruiter_email,
                                msg.as_string()
                            )

                        # Save Record
                        save_application(
                            company=company_name,
                            role=role,
                            recipient_email=recruiter_email,
                            status="Sent",
                        )

                        st.success(
                            f"✅ Application sent successfully to {recruiter_email}"
                        )

                    except smtplib.SMTPAuthenticationError:

                        st.error(
                            "SMTP Authentication Failed. "
                            "Please check Gmail App Password."
                        )

                    except Exception as e:

                        st.error(
                            f"Failed to send email: {str(e)}"
                        )

        else:

            st.info(
                "Please fill your Name and Email "
                "to preview the email."
            )

# ==================================================
# APPLICATION TRACKER TAB
# ==================================================

with tab2:

    st.subheader(
        "📊 Application Tracker"
    )

    applications = get_all_applications()

    if applications:

        st.table(
            [
                {
                    "ID": app[0],
                    "Date": app[1],
                    "Company": app[2],
                    "Role": app[3],
                    "Recipient Email": app[4],
                    "Status": app[5],
                }
                for app in applications
            ]
        )

    else:

        st.info(
            "No applications sent yet."
        )