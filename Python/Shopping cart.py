class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name] -= quantity

    def calculate_total(self):
        total_price = 0
        for item_name, quantity in self.items.items():
            # Replace the line below with your item price retrieval logic if needed
            # e.g., fetching the price from a database or a product catalog
            item_price = 10  # Default price for demonstration purposes
            total_price += item_price * quantity

        return total_price


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.add_item("Banana", 0.75, 2)
    cart.add_item("Orange", 2.0)
    cart.remove_item("Apple", 2)

    total_price = cart.calculate_total()
    print(f"Total price of the items in the shopping cart: ${total_price:.2f}")
