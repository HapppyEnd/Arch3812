from in_memory_model import IModelChangeObserver, ImodelChanger
from model_elements import Camera, Flash, PoligonalModel, Scene


class ModelStore(ImodelChanger):
    def __init__(self, change_observers: list[IModelChangeObserver]) -> None:
        self.models = [PoligonalModel(), ]
        self.scenes = [Scene(), ]
        self.flashes = [Flash(), ]
        self.cameras = [Camera(), ]

    def get_scena(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_changer(self, sender) -> None:
        return super().notify_changer(sender)
