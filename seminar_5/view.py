"""View module."""
from product import Product
from storage import Storage


class View():
    """Class View."""

    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def search_product(self, product: Product) -> Product:
        """Search product."""
        return self.storage.products[product.get_id()]

    def show_all_products(self) -> None:
        """Show all products."""
        for product in self.storage.products:
            print(product)
