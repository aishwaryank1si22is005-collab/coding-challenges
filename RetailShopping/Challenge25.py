# Function to get item code
def get_item_code():
    while True:
        code = input("Enter Item Code: ").strip()
        if code == "":
            print("Error: Item Code cannot be empty.")
        else:
            return code


# Function to get item description
def get_item_description():
    while True:
        description = input("Enter Item Description: ").strip()
        if description == "":
            print("Error: Description cannot be empty.")
        else:
            return description


# Function to get quantity with validation
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter Quantity (minimum 1): "))
            if quantity < 1:
                print("Error: Quantity must be at least 1.")
            else:
                return quantity
        except ValueError:
            print("Error: Enter a valid whole number.")


# Function to get price with validation
def get_price():
    while True:
        try:
            price = float(input("Enter Price per Item (>0): "))
            if price <= 0:
                print("Error: Price must be greater than 0.")
            else:
                return price
        except ValueError:
            print("Error: Enter a valid number.")




code = get_item_code()
description = get_item_description()
quantity = get_quantity()
price = get_price()

total = quantity * price


print("Item Code      :", code)
print("Description    :", description)
print("Quantity       :", quantity)
print("Price per Item : ₹", price)
print("Total Cost     : ₹", total)
