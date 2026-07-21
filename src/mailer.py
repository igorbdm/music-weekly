import os
import smtplib
from datetime import datetime
from email.message import EmailMessage


def get_settings():
    required_settings = ["SMTP_HOST", "SMTP_USERNAME", "SMTP_PASSWORD", "EMAIL_TO"]
    missing_settings = [setting for setting in required_settings if not os.getenv(setting)]

    if missing_settings:
        names = ", ".join(missing_settings)
        raise RuntimeError(f"Configurações de e-mail ausentes: {names}")

    return {
        "host": os.environ["SMTP_HOST"],
        "port": int(os.getenv("SMTP_PORT", "587")),
        "username": os.environ["SMTP_USERNAME"],
        "password": os.environ["SMTP_PASSWORD"],
        "sender": os.getenv("EMAIL_FROM", os.environ["SMTP_USERNAME"]),
        "recipient": os.environ["EMAIL_TO"],
    }


def send_newsletter(html):
    """Envia a newsletter e só retorna após o servidor aceitar a mensagem."""
    settings = get_settings()
    message = EmailMessage()
    message["Subject"] = f"Music Weekly — {datetime.now().strftime('%d/%m/%Y')}"
    message["From"] = settings["sender"]
    message["To"] = settings["recipient"]
    message.set_content("Abra este e-mail em um leitor que suporte HTML.")
    message.add_alternative(html, subtype="html")

    with smtplib.SMTP(settings["host"], settings["port"]) as server:
        server.starttls()
        server.login(settings["username"], settings["password"])
        server.send_message(message)
