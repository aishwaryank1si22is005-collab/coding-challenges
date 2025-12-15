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

# Function to get quantity
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

# Function to get price
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




items = []          # store all item details (for bill)
grand_total = 0     # sum of all items

while True:
    print("\n--- Enter Item Details ---")
    
    code = get_item_code()
    description = get_item_description()
    quantity = get_quantity()
    price = get_price()

    item_total = quantity * price
    grand_total += item_total

    # Store item in list
    items.append([code, description, quantity, price, item_total])

    # Continue?
    choice = input("Add another item? (yes/no): ").lower().strip()
    if choice != "yes":
        break




print("\n")
print("="*50)
print("               SHOPPING BILL")
print("="*50)
print(f"{'Code':<10}{'Description':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
print("-"*50)

for item in items:
    code, desc, qty, price, total = item
    print(f"{code:<10}{desc:<15}{qty:<5}{price:<10.2f}{total:<10.2f}")

print("-"*50)
print(f"{'GRAND TOTAL':<35} ₹ {grand_total:.2f}")
print("="*50)

