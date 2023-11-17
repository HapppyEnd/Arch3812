"""In memory model module."""
from abc import ABC, abstractmethod


class IModelChangeObserver(ABC):
    """ Abstract class IModelChangeObserver."""
    @abstractmethod
    def apply_update_model(self) -> None:
        """Abstract function."""


class ImodelChanger(ABC):
    """ Abstract class ImodelChanger."""
    @abstractmethod
    def notify_changer(self, sender) -> None:
        """Abstract function.

        Parameters:
            sender: any
        """
