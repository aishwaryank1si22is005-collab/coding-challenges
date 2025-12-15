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


# =================== MAIN PROGRAM ===================

items = []
grand_total = 0
total_quantity = 0

# Membership
while True:
    membership = input("Please specify membership status (y/n): ")
    if membership.lower() in ['y', 'n']:
        break
    print("Please enter a valid membership status.")

while True:
    print("\n--- Enter Item Details ---")

    code = get_item_code()
    description = get_item_description()
    quantity = get_quantity()
    price = get_price()

    # Base item total
    item_total = quantity * price

    # Promotional discount (10% if code starts with PR)
    promo_discount = 0
    if code.upper().startswith("PR"):
        promo_discount = item_total * 0.10
        item_total -= promo_discount

    # Update totals
    grand_total += item_total
    total_quantity += quantity

    # Store item including promo discount
    items.append([code, description, quantity, price, item_total, promo_discount])

    # Continue?
    choice = input("Add another item? (yes/no): ").lower().strip()
    if choice != "yes":
        break


# =================== APPLY DISCOUNTS ===================

discount_10 = 0
discount_5 = 0
discount_membership = 0

# Rule 1: 10% discount if grand total > 10,000
if grand_total > 10000:
    discount_10 = grand_total * 0.10
    grand_total -= discount_10

# Rule 2: 5% discount if total quantity > 20
if total_quantity > 20:
    discount_5 = grand_total * 0.05
    grand_total -= discount_5

# Rule 3: 2% membership discount
if membership.lower() == 'y':
    discount_membership = grand_total * 0.02
    grand_total -= discount_membership


# =================== APPLY TAX ===================

tax_rate = 0

if grand_total < 5000:
    tax_rate = 5
elif 5000 <= grand_total <= 20000:
    tax_rate = 10
else:
    tax_rate = 15

tax_amount = grand_total * (tax_rate / 100)
grand_total += tax_amount


# =================== PRINT SHOPPING BILL ===================

print("\n")
print("=" * 50)
print("               SHOPPING BILL")
print("=" * 50)
print(f"{'Code':<10}{'Description':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
print("-" * 50)

# Print each item
for item in items:
    code, desc, qty, price, total, promo_disc = item
    print(f"{code:<10}{desc:<15}{qty:<5}{price:<10.2f}{total:<10.2f}")

    if promo_disc > 0:
        print(f"{'':<10}{'PR Promo Applied':<15}{'':<5}{'':<10}-₹ {promo_disc:.2f}")

print("-" * 50)

# Print summary of all discounts
promo_total_discount = sum(item[5] for item in items)

if promo_total_discount > 0:
    print(f"{'PR Code Discounts:':<35} -₹ {promo_total_discount:.2f}")

if discount_10 > 0:
    print(f"{'10% Discount Applied:':<35} -₹ {discount_10:.2f}")

if discount_5 > 0:
    print(f"{'5% Quantity Discount:':<35} -₹ {discount_5:.2f}")

if discount_membership > 0:
    print(f"{'2% Membership Discount:':<35} -₹ {discount_membership:.2f}")

# Tax
print(f"{'Tax (' + str(tax_rate) + '%):':<35} +₹ {tax_amount:.2f}")

# Final total
print(f"{'FINAL GRAND TOTAL':<35} ₹ {grand_total:.2f}")
print("=" * 50)
