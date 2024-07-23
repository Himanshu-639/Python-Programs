class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def displayInfo(self):
        print(f"{self.name} - Price: ${self.price:.2f}")

availableItems = [
    Item("Laptop", 999.99, 10),
    Item("Headphones", 49.99, 20),
    Item("Smartphone", 599.99, 15),
    # Add more items as needed
]

def displayAvailableItems(items):
    print("Available Items:")
    for item in items:
        item.displayInfo()

displayAvailableItems(availableItems)


