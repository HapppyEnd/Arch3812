"""Model Store module."""
from in_memory_model import IModelChangeObserver, ImodelChanger
from model_elements import Camera,  PoligonalModel, Scene
from service import Texture


class ModelStore(ImodelChanger):
    """class ModelStore implements ImodelChanger."""

    def __init__(self, change_observers: list[IModelChangeObserver]) -> None:
        self.models = [PoligonalModel(textures=Texture()), ]
        self.flashes = []
        self.cameras = [Camera(), ]
        self.scenes = [Scene(id_=1, models=self.models,
                             flashes=self.flashes, cameras=self.cameras)]

        self.change_observers = change_observers

    def get_scena(self, id_) -> Scene | None:
        """Return scene if exist.

        Parameters:
            id: id scene

        Returns:
           scene: Scene or None(if scene not exist)
        """
        for scene in self.scenes:
            if scene.id == id_:
                return scene
        return None

    def notify_changer(self, sender) -> None:
        return sender
