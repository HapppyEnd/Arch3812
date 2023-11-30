"""Storage module."""
from delivery import Delivery
from product import Product
from order import Order
from user import User


class Storage():
    """Class Storage."""

    def __init__(self) -> None:
        self.products: list[Product] = []
        self.users: list[User] = []
        self.orders: list[Order] = []
        self.list_delivery: list[Delivery] = []

        self.bd = {
            'Product': self.products,
            'User': self.users,
            'Order': self.orders,
            'Delivery': self.list_delivery,
        }

    def add(self, element: object) -> None:
        """Add to storage."""
        self.bd.get(type(element).__name__).append(element)

    def remove(self, element: object) -> None:
        """Remove from storage."""
        data: list = self.bd.get(type(element).__name__)
        if element in data:
            data.remove(element)

    def read(self, element: object) -> None:
        """Show all info."""
        return self.bd.get(element.__name__)

    def update(self, element: object) -> None:
        """Edit info."""
        data: list = self.bd.get(type(element).__name__)
        data.remove(element)
        data.append(element)
