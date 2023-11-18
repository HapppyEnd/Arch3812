"""Abstract classes"""
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    """Abstract class ItemFabric."""
    @abstractmethod
    def create_item(self) -> None:
        """Create item."""


class IGameItem(ABC):
    """Abstract class IGameItem."""
    @abstractmethod
    def open(self) -> None:
        """Open reward."""
