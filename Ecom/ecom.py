import os

print("\n   *** Welcome to the Amazkart Shopping ***   \n")

username = input("Enter Your Username: ")
file_path = "Data.txt"
if not os.path.isfile(file_path):
    with open(file_path, "w") as file:
        pass

with open(file_path, "a+") as file:
    file.seek(0)
    data = file.read()
    if username in data:
        print(f"Good to see you, {username}!")
    else:
        print("It seems you have not registered with us yet.\n")
        rchoice = input("Enter 1 to Register Now else 2 to go back! ")

        if rchoice == "1":
            name_reply = input("Enter Your Name: ")
            file.write(name_reply + "\n")
            print(f"Thank you, {name_reply}, for registering!")
        else:
            print("Exiting...")

# The list should be defined as a set for proper membership check
categories = {"Electronics", "Fashion", "Grocery", "Mobiles"}

def electronics():
    

def home():
    print(f"\nAvailable Categories: {', '.join(categories)}")
    cchoice = input("Enter Your Choice: ")

# Call the function
home()



'''

availableItems = [
    ("Laptop", 999.99, 10),
    ("Headphones", 49.99, 20),
    ("Smartphone", 599.99, 15),
    # Add more items as needed
]

def displayAvailableItems(items):
    print("Available Items:")
    for item in items:
        item.displayInfo()

displayAvailableItems(availableItems)


'''