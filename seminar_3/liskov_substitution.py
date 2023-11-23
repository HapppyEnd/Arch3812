"""Переписать код в соответствии с Liskov Substitution Principle:
"""


class Rectangle:
    """Class Rectangle."""

    def __init__(self) -> None:
        self.width = 0
        self.height = 0

    def set_width(self, width: int) -> None:
        """Set width."""
        self.width = width

    def set_height(self, height: int) -> None:
        """Set height."""
        self.height = height

    def area(self) -> int:
        """Return area."""
        return self.width * self.height


class Square(Rectangle):
    """Class Square."""

    def set_width(self, width) -> None:
        self.width = width
        self.height = width

    def set_height(self, height) -> None:
        self.width = height
        self.height = height

    def area(self) -> int:
        return self.width * self.height
