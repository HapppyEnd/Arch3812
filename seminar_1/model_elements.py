from service import Angle3D, Color, Point3D, Poligon


class PoligonalModel():

    def __init__(self) -> None:
        self.poligons = [Poligon(), ]
        self.textures = []


class Flash():

    def __init__(self, power: float, color: Color) -> None:
        self.location = Point3D()
        self.angle = Angle3D()
        self.color = color
        self.power = power

    def rotate(self, angle_3d) -> None:
        pass

    def move(self, point_3d) -> None:
        pass


class Camera():
    def __init__(self) -> None:
        self.location = Point3D()
        self.angle = Angle3D()

    def rotate(self, angle_3d: Angle3D) -> None:
        pass

    def move(self, point_3d: Point3D) -> None:
        pass


class Scene():
    def __init__(
            self, id, models: list[PoligonalModel], flashes: list[Flash]
    ) -> None:
        self.id = id
        self.models = models
        self.flashes = flashes

    def method_1(self, models: list[PoligonalModel]) -> list:
        return models

    def method_2(
            self, models: list[PoligonalModel], flashes: list[Flash]) -> list:
        return models + flashes
