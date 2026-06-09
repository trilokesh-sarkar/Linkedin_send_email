"""
SQLite database module for tracking job applications.
Compatible with Streamlit Cloud (ephemeral filesystem).
"""

import sqlite3
import os
import tempfile
from datetime import datetime

# On Streamlit Cloud the app dir may be read-only.
# Use /tmp (Linux) or system temp dir for the DB file.
DB_NAME = os.path.join(tempfile.gettempdir(), "applications.db")


def get_connection():
    """Get a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    return conn


def init_db():
    """Initialize the applications table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            recipient_email TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def save_application(company: str, role: str, recipient_email: str, status: str):
    """Save a new application record."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO applications (date, company, role, recipient_email, status)
        VALUES (?, ?, ?, ?, ?)
    """,
        (datetime.now().strftime("%Y-%m-%d %H:%M"), company, role, recipient_email, status),
    )
    conn.commit()
    conn.close()


def get_all_applications():
    """Retrieve all application records, most recent first."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
