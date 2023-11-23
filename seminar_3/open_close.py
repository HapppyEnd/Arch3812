"""Переписать код SpeedCalculation в соответствии с
Open-Closed Principle."""
from abc import ABC, abstractmethod


class SpeedCalculation(ABC):
    """Abstract class SpeedCalculation."""

    @abstractmethod
    def calculate_allowed_speed(self) -> float:
        """Calculate allowed speed."""


class Vehicle(SpeedCalculation):
    """Class Vehicle."""

    def __init__(self, max_speed: float, transport_type: str) -> None:
        self.max_speed = max_speed
        self.transport_type = transport_type

    def get_max_speed(self) -> float:
        """Get max speed."""
        return self.max_speed

    def get_type(self) -> str:
        """Get transport type."""
        return self.transport_type.lower()

    def calculate_allowed_speed(self) -> float:
        return self.get_max_speed() * 0.4


class Car(Vehicle):
    """Class Car."""

    def calculate_allowed_speed(self) -> float:
        return self.get_max_speed() * 0.8


class Bus(Vehicle):
    """Class Bus."""

    def calculate_allowed_speed(self) -> float:
        return self.get_max_speed() * 0.6


car = Car(100, 'CAR')
bus = Bus(60, 'bus')
vehicle = Vehicle(15, 'Vehicle')
print(f'{car.calculate_allowed_speed()} - {car.get_type()}')
print(f'{bus.calculate_allowed_speed()} - {bus.get_type()}')
print(f'{vehicle.calculate_allowed_speed()} - {vehicle.get_type()}')
