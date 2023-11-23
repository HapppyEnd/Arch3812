"""Переписать код в соответствии с Interface Segregation Principle:
Подсказка: круг не объемная фигура и этому классу
не нужен метод volume()."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""
    @abstractmethod
    def area(self) -> float:
        """Return area."""


class Volume(ABC):
    """Abstract class Volume."""
    @abstractmethod
    def volume(self) -> float:
        """Return volume."""


class Circle(Shape):
    """Class circle."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 2 * math.pi * self.radius


class Cube(Shape, Volume):
    """Class Cube."""

    def __init__(self, edge: float) -> None:
        self.edge = edge

    def area(self) -> float:
        return 6 * self.edge * self.edge

    def volume(self) -> float:
        return self.edge * self.edge * self.edge
