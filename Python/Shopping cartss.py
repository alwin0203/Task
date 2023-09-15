class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name] -= quantity

    def calculate_total(self, price, quantity):
        total_price = 0
        for item_name, quantity in self.items.items(): 
            total_price += price * quantity

        return total_price


def main():
    cart = ShoppingCart()

    while True:
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Calculate total price")
        print("4. Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            item_name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            cart.add_item(item_name, price, quantity)
        elif choice == 2:
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            cart.remove_item(item_name, quantity)
        elif choice == 3:
            total_price = cart.calculate_total(price,quantity)
            print(f"Total price of the items in the shopping cart: ${total_price:.2f}")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
