"""Order module."""


from product import Product
from user import User


class Order():
    """Class Order."""

    def __init__(self, user: User) -> None:
        self.user = user
        self.products: list[Product] = []
        self.issued = False

    def add_product_to_order(self, product: Product) -> None:
        """Add product to order."""
        if not self.issued:
            self.products.append(product)
        raise RuntimeError(
            'Impossible to add products, the order has been sent to delivery.')

    def delete_product_from_order(self, product: Product) -> None:
        """Delete product from order."""
        if not self.issued and not self.products:
            self.products.remove(product)
        raise RuntimeError(
            'Impossible to delete products, '
            'the order has been sent to delivery or yor order is empty.')
