"""Model elements module."""
from service import Angle3D, Color, Point3D, Poligon, Texture


class PoligonalModel():
    """Class PoligonalModel."""

    def __init__(self, textures: Texture) -> None:
        self.poligons = []
        self.textures = textures
        self.poligons.append(Poligon())


class Flash():
    """class Flash"""

    def __init__(self, power: float, color: Color) -> None:
        self.location = Point3D()
        self.angle = Angle3D()
        self.color = color
        self.power = power

    def rotate(self, angle_3d) -> None:
        """Rotate flash.

        Parameters:
            angle_3d: instance Angle3D
        """

    def move(self, point_3d) -> None:
        """Move flash.

       Parameters:
           point_3d: instance Point3D
       """


class Camera():
    """Class Camera."""

    def __init__(self) -> None:
        self.location = Point3D()
        self.angle = Angle3D()

    def rotate(self, angle_3d: Angle3D) -> None:
        """Rotate camera.

        Parameters:
            angle_3d: instance Angle3D
        """

    def move(self, point_3d: Point3D) -> None:
        """Move camera.

       Parameters:
           point_3d: instance Point3D

       """


class Scene():
    """Class Scene."""

    def __init__(
            self, id_: int, models: list[PoligonalModel], flashes: list[Flash]
    ) -> None:
        self.id = id_
        if len(models) > 0:
            self.models = models
        else:
            raise RuntimeError('There should be one model.')
        if len(flashes) > 0:
            self.flashes = flashes
        else:
            raise RuntimeError('There should be one flash.')

    def method_1(self, models: list[PoligonalModel]) -> list:
        """Return models list.

         Parameters:
            models: list PoligonalModel

        Returns:
            list: list PoligonalModel

            """
        return models

    def method_2(
            self, models: list[PoligonalModel], flashes: list[Flash]) -> list:
        """Return list models + flashes.

        Parameters:
            models: list[PoligonalModel]
            flashes: list[Flash]

        Returns:
            list: list PoligonalModel + list Flash

            """
        return models + flashes
