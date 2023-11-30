"""Product module."""


class Product():
    """class Product."""

    def __init__(self, product_id: int, name: str, description: str,
                 price: float) -> None:
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.discount_price = 0

    def get_id(self) -> int:
        """Get product id."""
        return self.product_id

    def set_price(self, price: float) -> None:
        """Set product price."""
        self.price = price

    def discount(self, discount: int) -> None:
        """Discount."""
        self.discount_price = self.price - self.price * discount

    def __str__(self) -> str:
        """Get full info about product."""
        return f'{self.name} - {self.description}. price: {self.price}'
