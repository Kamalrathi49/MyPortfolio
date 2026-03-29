import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from app.core.config import get_settings

logger = logging.getLogger("app.email")


def send_contact_email(
    name: str,
    email: str,
    subject: str,
    message: str,
    company: Optional[str],
) -> None:
    settings = get_settings()
    to_addr = settings.effective_notify_to()
    from_addr = settings.effective_smtp_from()
    body_parts = [
        f"From: {name} <{email}>",
        f"Subject: {subject}",
    ]
    if company:
        body_parts.append(f"Company: {company}")
    body_parts.append("")
    body_parts.append(message)
    body = "\n".join(body_parts)
    msg = MIMEMultipart()
    msg["Subject"] = f"[Portfolio] {subject}"
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.attach(MIMEText(body, "plain", "utf-8"))
    try:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=30) as smtp:
            smtp.starttls()
            smtp.login(settings.smtp_user, settings.smtp_password)
            smtp.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception:
        logger.exception("smtp_send_failed")
        raise
