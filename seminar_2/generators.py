"""Generator rewards module."""
from interfaces import ItemFabric
from rewards import (Bronze, ChestSurprise, Gem, Gold, Nothing, Platinum,
                     Sapphire, Silver)


class BronzeGenerator(ItemFabric):
    """Class bronze reward generator."""

    def create_item(self) -> Bronze:
        """Bronze reward."""
        return Bronze()


class ChestSurpriseGenerator(ItemFabric):
    """Class ChestSurprise reward generator."""

    def create_item(self) -> ChestSurprise:
        """ChestSurprise reward."""
        return ChestSurprise()


class GemGenerator(ItemFabric):
    """Class Gem reward generator."""

    def create_item(self) -> Gem:
        """Gem reward."""
        return Gem()


class GoldGenerator(ItemFabric):
    """Class Gold reward generator."""

    def create_item(self) -> Gold:
        """Gold reward."""
        return Gold()


class NothingGenerator(ItemFabric):
    """Class Not reward generator."""

    def create_item(self) -> Nothing:
        """Not reward."""
        return Nothing()


class PlatinumGenerator(ItemFabric):
    """Class Platinum reward generator."""

    def create_item(self) -> Platinum:
        """Platinum reward."""
        return Platinum()


class SapphireGenerator(ItemFabric):
    """Class Sapphire reward generator."""

    def create_item(self) -> Sapphire:
        """Sapphire reward."""
        return Sapphire()


class SilverGenerator(ItemFabric):
    """Class Silver reward generator."""

    def create_item(self) -> Silver:
        """Silver reward."""
        return Silver()
