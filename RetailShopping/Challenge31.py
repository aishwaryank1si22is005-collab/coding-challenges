# ---------- INPUT FUNCTIONS ----------

def get_item_code():
    while True:
        code = input("Enter Item Code: ").strip()
        if code == "":
            print("Error: Item Code cannot be empty.")
        else:
            return code


def get_item_description():
    while True:
        description = input("Enter Item Description: ").strip()
        if description == "":
            print("Error: Description cannot be empty.")
        else:
            return description


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

# Membership input
while True:
    membership = input("Please specify membership status (y/n): ").lower()
    if membership in ['y', 'n']:
        break
    print("Please enter a valid membership status.")

# Item entry loop
while True:
    print("\n--- Enter Item Details ---")

    code = get_item_code()
    description = get_item_description()
    quantity = get_quantity()
    price = get_price()

    item_total = quantity * price

    # Promo discount: 10% if code starts with PR
    promo_discount = 0
    if code.upper().startswith("PR"):
        promo_discount = item_total * 0.10
        item_total -= promo_discount

    grand_total += item_total
    total_quantity += quantity

    items.append([code, description, quantity, price, item_total, promo_discount])

    choice = input("Add another item? (yes/no): ").lower()
    if choice != "yes":
        break

# Payment method input
while True:
    payment_method = input("Select payment method (cash/card): ").lower()
    if payment_method in ['cash', 'card']:
        break
    print("Please enter a valid payment method (cash/card).")




discount_10 = 0
discount_5 = 0
discount_membership = 0

if grand_total > 10000:
    discount_10 = grand_total * 0.10
    grand_total -= discount_10

if total_quantity > 20:
    discount_5 = grand_total * 0.05
    grand_total -= discount_5

if membership == 'y':
    discount_membership = grand_total * 0.02
    grand_total -= discount_membership




if grand_total < 5000:
    tax_rate = 5
elif grand_total <= 20000:
    tax_rate = 10
else:
    tax_rate = 15

tax_amount = grand_total * (tax_rate / 100)
grand_total += tax_amount




surcharge = 0
if payment_method == 'card':
    surcharge = grand_total * 0.02
    grand_total += surcharge




print("\n" + "=" * 50)
print("               SHOPPING BILL")
print("=" * 50)
print(f"{'Code':<10}{'Description':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
print("-" * 50)

for item in items:
    code, desc, qty, price, total, promo_disc = item
    print(f"{code:<10}{desc:<15}{qty:<5}{price:<10.2f}{total:<10.2f}")
    if promo_disc > 0:
        print(f"{'':<10}{'PR Promo Applied':<15}{'':<5}{'':<10}-₹ {promo_disc:.2f}")

print("-" * 50)

promo_total_discount = sum(item[5] for item in items)
if promo_total_discount > 0:
    print(f"{'PR Code Discounts:':<35} -₹ {promo_total_discount:.2f}")

if discount_10 > 0:
    print(f"{'10% Bill Discount:':<35} -₹ {discount_10:.2f}")

if discount_5 > 0:
    print(f"{'5% Quantity Discount:':<35} -₹ {discount_5:.2f}")

if discount_membership > 0:
    print(f"{'2% Membership Discount:':<35} -₹ {discount_membership:.2f}")

print(f"{'Tax (' + str(tax_rate) + '%):':<35} +₹ {tax_amount:.2f}")
print(f"{'Payment Method:':<35} {payment_method.upper()}")

if surcharge > 0:
    print(f"{'Card Surcharge (2%):':<35} +₹ {surcharge:.2f}")

print(f"{'FINAL PAYABLE AMOUNT':<35} ₹ {grand_total:.2f}")
print("=" * 50)
