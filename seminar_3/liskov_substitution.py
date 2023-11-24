"""Переписать код в соответствии с Liskov Substitution Principle:
"""


class Quadrangle:
    """Class Quadrangle."""

    def area(self) -> None:
        """Calculate area."""


class Rectangle(Quadrangle):
    """Class Rectangle."""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


class Square(Quadrangle):
    """Class Square."""

    def __init__(self, length: int) -> None:
        self.length = length

    def area(self) -> int:
        return self.length * self.length
