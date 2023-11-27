"""Ticket module."""

from dataclasses import dataclass
from datetime import datetime
import decimal


@dataclass
class Ticket:
    """class Ticket."""
    price: decimal
    date: datetime
    start_zone: int
    finish_zone: int
    is_luggage: bool
    place: int
    road_number: int

    def get_price(self) -> decimal:
        """Return price."""
        return self.price

    def get_date(self) -> datetime:
        """Return date."""
        return self.date

    def get_start_zone(self) -> int:
        """Return start zone."""
        return self.start_zone

    def get_finish_zone(self) -> int:
        """Return finish zone."""
        return self.finish_zone

    def get_place(self) -> int:
        """Return place."""
        return self.place

    def get_road_number(self) -> int:
        """Return road number."""
        return self.road_number

    def get_is_luggage(self) -> bool:
        """Return true if luggage is or false if not."""
        return self.is_luggage

    def buy_ticket(self) -> None:
        """Buy ticket."""

    def refund_ticket(self) -> None:
        """Refund ticket."""
