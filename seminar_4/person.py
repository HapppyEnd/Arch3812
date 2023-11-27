"""Person module."""
from dataclasses import dataclass


@dataclass
class Person:
    """Class Person."""
    person_id: int
    fio: str
    card_number: int
    hash_pass: int
    login: str

    def get_id(self) -> int:
        """Return id."""
        return self.person_id

    def get_fio(self) -> str:
        """Return full name."""
        return self.fio

    def get_card_number(self) -> str:
        """Return card number."""
        return self.card_number

    def set_card_number(self, card_number) -> None:
        """Set card number."""
        self.card_number = card_number

    def get_login(self) -> str:
        """Return login."""
        return self.login

    def set_login(self, login: str) -> None:
        """Set login."""
        self.login = login

    def get_hash_pass(self) -> int:
        """Return Hash pass."""
        return self.hash_pass

    def set_hash_pass(self, hash_pass: int) -> None:
        """Set Hash pass."""
        self.hash_pass = hash_pass

    def registration(self) -> None:
        """User registration."""

    def authorization(self) -> None:
        """User authorization."""

    def delete_user(self) -> None:
        """Delete user."""
