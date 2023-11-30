"""User module."""
from dataclasses import dataclass


@dataclass
class User():
    """class User."""

    user_id: int
    fio: str
    login: str
    password: str
    address: str

    def get_id(self) -> int:
        """Get user id."""
        return self.user_id

    def get_fio(self) -> str:
        """Return full name."""
        return self.fio

    def get_login(self) -> str:
        """Return login."""
        return self.login

    def set_login(self, login: str) -> None:
        """Set login."""
        self.login = login

    def get_password(self) -> str:
        """Return password."""
        return self.password

    def set_password(self, password: int) -> None:
        """Set password."""
        self.password = password

    def authorization(self, login: str, password: str) -> bool:
        """User authorization."""
        if self.login == login & self.password == password:
            return True
        return False
