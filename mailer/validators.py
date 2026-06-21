import re
from typing import Pattern


class EmailValidator:
    PATTERN: Pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    @staticmethod
    def validate(email: str) -> bool:
        """Waliduj format emaila (upraszczony, zgodny z RFC-like pattern)."""
        if not email or not isinstance(email, str):
            return False
        return bool(EmailValidator.PATTERN.match(email.strip()))
