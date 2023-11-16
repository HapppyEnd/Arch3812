from abc import ABC, abstractmethod


class IModelChangeObserver(ABC):
    @abstractmethod
    def apply_update_model(self) -> None:
        pass


class ImodelChanger(ABC):
    @abstractmethod
    def notify_changer(self, sender) -> None:
        pass
