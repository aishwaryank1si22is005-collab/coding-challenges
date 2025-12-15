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




items = []          
grand_total = 0     
total_quantity = 0  

while True:
    membership=input("Please specify the membership statur(y/n):")
    if membership.lower()=='y' or membership.lower()=='n':
        break
    else:
        print("Please Enter the valid membership status")

while True:
    print("\n--- Enter Item Details ---")
    
    code = get_item_code()
    description = get_item_description()
    quantity = get_quantity()
    price = get_price()

    item_total = quantity * price
    grand_total += item_total
    total_quantity += quantity

    # Store item in list
    items.append([code, description, quantity, price, item_total])

    # Continue?
    choice = input("Add another item? (yes/no): ").lower().strip()
    if choice != "yes":
        break




discount_10 = 0
discount_5 = 0
discount_membership=0

# Rule 1: 10% discount if grand total > 10000
if grand_total > 10000:
    discount_10 = grand_total * 0.10
    grand_total -= discount_10

# Rule 2: Additional 5% discount if total quantity > 20
if total_quantity > 20:
    discount_5 = grand_total * 0.05
    grand_total -= discount_5

#Rule3 : Additional 2% discount if user has membership
if membership.lower()=='y':
    discount_membership=grand_total*0.02
    grand_total-=discount_membership


#Tax Caclulation


tax_rate = 0
tax_amount = 0

if grand_total < 5000:
    tax_rate = 5
elif 5000 <= grand_total <= 20000:
    tax_rate = 10
else:
    tax_rate = 15

tax_amount = grand_total * (tax_rate / 100)
grand_total += tax_amount




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

# Show discounts clearly if applied
if discount_10 > 0:
    print(f"{'10% Discount Applied:':<35} -₹ {discount_10:.2f}")

if discount_5 > 0:
    print(f"{'Additional 5% Qty Discount:':<35} -₹ {discount_5:.2f}")

if discount_membership>0:
    print(f"{'2% Membership Discount:':<35} -₹ {discount_membership:.2f}")

print(f"{'Tax (' + str(tax_rate) + '%):':<35} +₹ {tax_amount:.2f}")

print(f"{'FINAL GRAND TOTAL':<35} ₹ {grand_total:.2f}")
print("="*50)
