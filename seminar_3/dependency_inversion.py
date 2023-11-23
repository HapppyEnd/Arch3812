"""Переписать код в соответствии с Dependency Inversion Principle:
Разорвать зависимость классов Car и PetrolEngine.
У машины же может быть DieselEngine."""
from abc import ABC, abstractmethod


class Engine(ABC):
    """Abstract class Engine."""
    @abstractmethod
    def start(self) -> None:
        """Start."""


class Car(Engine):
    """Class Car."""

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def start(self) -> None:
        self.engine.start()


class PetrolEngine(Engine):
    """Class PetrolEngine"""

    def start(self) -> None:
        pass
