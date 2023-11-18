"""Rewards module."""
from interfaces import IGameItem


class Gold(IGameItem):
    """Class Gold reward."""

    def open(self) -> None:
        print('Gold!')


class Silver(IGameItem):
    """Class Silver reward."""

    def open(self) -> None:
        print('Silver!')


class Gem(IGameItem):
    """Class Gem reward."""

    def open(self) -> None:
        print('Gem!')


class Bronze(IGameItem):
    """Class Bronze reward."""

    def open(self) -> None:
        print('Bronze!')


class Platinum(IGameItem):
    """Class Platinum reward."""

    def open(self) -> None:
        print('Platinum!')


class Sapphire(IGameItem):
    """Class Sapphire reward."""

    def open(self) -> None:
        print('Sapphire!')


class ChestSurprise(IGameItem):
    """Class Surprise reward."""

    def open(self) -> None:
        print('Chest with surprise!')


class Nothing(IGameItem):
    """Class not reward"""

    def open(self) -> None:
        print('You get nothing, lucky another time.')
