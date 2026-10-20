class Product:
    def __init__(self, name, price, quantity):
        # Validierung
        if not name or name.strip() == "":
            raise Exception("Product name cannot be empty.")

        if price < 0:
            raise Exception("Price cannot be negative.")

        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception("Product is not active.")

        if quantity <= 0:
            raise Exception("Quantity must be positive.")

        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
