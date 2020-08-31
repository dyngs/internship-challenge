products = [
    {"name": "Prod1", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod2", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod3", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod4", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod5", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod6", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod7", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod8", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod9", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
    {"name": "Prod10", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
]
obj_list = []


class ParentProduct:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name of this product is {self.name}")

class Product(ParentProduct):
    def __init__(self, name, amount, price):
        super().__init__(name)
        self.amount = amount
        self.price = price

    def show_price(self, currency: str):
        print(self.name + "price is" + str(self.price))

    def show_amount(self):
        print(self.name + "amount is" + str(self.amount))

    def calculate_total_value(self):
        return self.amount*self.price

    def get_name(self):
        return self.name



