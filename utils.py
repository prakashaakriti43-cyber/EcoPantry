import smtplib
import ssl
import certifi
from datetime import datetime, date

import streamlit as st

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def apply_custom_sidebar_style():
    """Applies EcoPantry sidebar styling."""

    st.markdown(
        """
        <style>

        [data-testid="stSidebar"] {
            background-color: #121614 !important;
            border-right: 1px solid rgba(0, 255, 135, 0.15) !important;
        }

        [data-testid="stSidebarNav"] a {
            color: #C0C8C2 !important;
            border-radius: 8px !important;
            margin: 2px 8px !important;
            transition: all 0.2s ease !important;
        }

        [data-testid="stSidebarNav"] a:hover {
            color: #00FF87 !important;
            background-color: rgba(0, 255, 135, 0.08) !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


def check_and_send_notifications(
    pantry_items,
    user_email,
    days_threshold=3
):
    """
    Sends an EcoPantry expiry reminder email.

    IMPORTANT:
    Email credentials are read ONLY from
    .streamlit/secrets.toml
    """

    # =====================================================
    # GET EMAIL CREDENTIALS
    # =====================================================

   try:
    sender_email = st.secrets["email"]["sender_email"]
    sender_password = st.secrets["email"]["sender_password"]

except Exception:
    return (
        False,
        "❌ Email settings are missing. "
        "Please check your Streamlit Secrets."
    )


    # =====================================================
    # BASIC EMAIL VALIDATION
    # =====================================================

    if not user_email or "@" not in user_email:

        return (
            False,
            "❌ Please enter a valid recipient email address."
        )


    # =====================================================
    # CHECK EXPIRING ITEMS
    # =====================================================

    today = date.today()

    expiring_items = []
    all_items = []


    for item in pantry_items:

        name = str(
            item.get("name", "Unknown Item")
        ).strip()

        expiry = item.get("expiry_date")


        if not expiry:
            continue


        try:

            # Handles:
            # 2026-08-15
            # 2026-08-15 00:00:00

            expiry_string = str(
                expiry
            ).split(" ")[0]

            expiry_date = datetime.strptime(
                expiry_string,
                "%Y-%m-%d"
            ).date()

        except Exception:

            continue


        days_left = (
            expiry_date - today
        ).days


        all_items.append(
            f"{name} — {days_left} days left"
        )


        if days_left < 0:

            expiring_items.append(
                f"🔴 {name} — EXPIRED "
                f"({abs(days_left)} days ago)"
            )

        elif days_left == 0:

            expiring_items.append(
                f"🚨 {name} — EXPIRES TODAY"
            )

        elif days_left <= days_threshold:

            expiring_items.append(
                f"⚠️ {name} — Expires in "
                f"{days_left} days"
            )


    # =====================================================
    # CREATE EMAIL
    # =====================================================

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = user_email

    message["Subject"] = (
        "🌱 EcoPantry — Pantry Expiry Alert"
    )


    body = (
        "🌱 ECOPANTRY\n"
        "Pantry Expiry Alert\n"
        "==============================\n\n"
    )


    if expiring_items:

        body += (
            "⚠️ ITEMS NEEDING YOUR ATTENTION\n\n"
        )

        body += "\n".join(
            expiring_items
        )

        body += "\n\n"


    else:

        body += (
            "🎉 Great news!\n\n"
            "You currently have no pantry items "
            f"expiring within {days_threshold} days.\n\n"
        )


    if all_items:

        body += (
            "📦 PANTRY OVERVIEW\n\n"
        )

        body += "\n".join(
            all_items
        )

        body += "\n\n"


    body += (
        "Open your EcoPantry dashboard to "
        "manage your inventory.\n\n"
        "— EcoPantry"
    )


    message.attach(
        MIMEText(
            body,
            "plain",
            "utf-8"
        )
    )


    # =====================================================
    # SEND THROUGH GMAIL SMTP
    # =====================================================

    try:

        context = ssl.create_default_context(
            cafile=certifi.where()
        )


        with smtplib.SMTP(
            "smtp.gmail.com",
            587,
            timeout=30
        ) as server:

            server.ehlo()

            server.starttls(
                context=context
            )

            server.ehlo()

            server.login(
                sender_email,
                sender_password
            )

            server.send_message(
                message
            )


        return (
            True,
            f"📧 Reminder successfully sent to "
            f"{user_email}!"
        )


    except smtplib.SMTPAuthenticationError:

        return (
            False,
            "❌ Gmail authentication failed. "
            "Check your sender email and Gmail App Password "
            "in .streamlit/secrets.toml."
        )


    except smtplib.SMTPException as e:

        return (
            False,
            f"❌ Gmail could not send the email: {e}"
        )


    except Exception as e:

        return (
            False,
            f"❌ Email failed: {e}"
        )
