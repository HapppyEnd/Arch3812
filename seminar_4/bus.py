"""Bus route and bus stop."""
from dataclasses import dataclass


@dataclass
class BusStop:
    """Class BusStop."""
    bus_stop_id: int
    name: str
    attitude: float
    latitude: float

    def get_id(self) -> int:
        """Return id."""
        return self.bus_stop_id

    def get_name(self) -> str:
        """Return name of bus stop."""
        return self.name

    def get_attitude(self) -> float:
        """Return attitude."""
        return self.attitude

    def get_latitude(self) -> float:
        """Return latitude."""
        return self.latitude


@dataclass
class BusRoute:
    """Class BusRoute."""
    bus_route_id: int
    remark: str
    capasity: int
    bus_stops: list[BusStop]

    def get_id(self) -> int:
        """Return id."""
        return self.bus_route_id

    def get_remark(self) -> str:
        """Return remark."""
        return self.remark

    def get_capacity(self) -> int:
        """Return capacity."""
        return self.capasity

    def get_bus_stops(self) -> list:
        """Return all bus stops."""
        return self.bus_stops
