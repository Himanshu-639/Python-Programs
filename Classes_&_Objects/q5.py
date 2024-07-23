class Item:
    
    def __init__(self, name, price, quantity):
        self.price=price
        self.name=name
        self.quantity=quantity
        

    def purchase(self, quantityPurchased):
        self.quantity-=quantityPurchased
        payingAmount=self.price*quantityPurchased
        return ('Amount Payable : '+ str(payingAmount))

    def increaseStock(self, newQuantity):
        self.quantity+=newQuantity
        return self.quantity
        

    def display(self):
        s='Name: '+self.name+'\n Price: '+str(self.price)
        print(s)
    
availableItems = [
    Item("Laptop", 999.99, 10),
    Item("Headphones", 49.99, 20),
    Item("Smartphone", 599.99, 15),
    # Add more items as needed
]
    
def displayItems(items):
        print("Available Items : ")
        for item in items:
            item.display()
displayItems(availableItems)

#i1 = Item('Desi Katta', 2000, 65000)
#print(i1.purchase(4))

newItemData = {"name": "Tablet", "price": 299.99, "quantity": 8}
newItem = Item(**newItemData)
availableItems.append(newItem)

displayItems(availableItems)