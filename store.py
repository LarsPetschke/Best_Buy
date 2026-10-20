from products import Product

class Store:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        # Summe aller Mengen
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> list:
        # Nur aktive Produkte zurückgeben
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        """
        shopping_list = [(product, quantity), (product, quantity)]
        """
        total_price = 0.0

        for product, amount in shopping_list:
            total_price += product.buy(amount)

        return total_price
