from typing import List, Set


class SubscriberManager:
    """Prosty menedżer subskrybentów w pamięci (do przykładów i testów)."""

    def __init__(self) -> None:
        self._subs: Set[str] = set()

    def add(self, email: str) -> bool:
        if email in self._subs:
            return False
        self._subs.add(email)
        return True

    def remove(self, email: str) -> bool:
        try:
            self._subs.remove(email)
            return True
        except KeyError:
            return False

    def list(self) -> List[str]:
        return sorted(self._subs)
