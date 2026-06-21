from typing import Dict, Optional
import smtplib
import os


class EmailSender:
    """Prosty wrapper nad smtplib do testów i przykładu."""

    def __init__(self, smtp_host: Optional[str] = None, smtp_port: Optional[int] = None) -> None:
        self.host = smtp_host or os.getenv("SMTP_HOST", "localhost")
        self.port = smtp_port or int(os.getenv("SMTP_PORT", "25"))

    def send(self, to_email: str, subject: str, body: str) -> Dict[str, Optional[str]]:
        """Wyślij wiadomość. W testach smtplib.SMTP jest mockowane."""
        try:
            with smtplib.SMTP(self.host, self.port) as smtp:
                message = f"Subject: {subject}\n\n{body}"
                smtp.sendmail("noreply@example.com", to_email, message)
            return {"success": True, "error": None}
        except Exception as e:
            return {"success": False, "error": str(e)}
