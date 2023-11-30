"""Delivery module."""
from datetime import datetime
from order import Order


class Delivery():
    """Class Delivery."""

    def __init__(self, order: Order, date: datetime) -> None:
        self.order = order
        self.date = date
        self.status = False

    def delivery_success(self) -> None:
        """Order delivered."""
        self.status = True

    def change_date(self, date: datetime) -> None:
        """Change delivery date."""
        self.date = date
