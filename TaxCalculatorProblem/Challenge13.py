def get_positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

taxable_income = get_positive_number("Enter Taxable Income: ")

tax = 0

if taxable_income <= 300000:
    tax = 0

elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05

elif taxable_income <= 900000:
    tax = (300000 * 0) + (300000 * 0.05) + (taxable_income - 600000) * 0.10

elif taxable_income <= 1200000:
    tax = (300000 * 0) + (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15

elif taxable_income <= 1500000:
    tax = (300000 * 0) + (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20

else:
    tax = (300000 * 0) + (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30

if taxable_income <= 700000:
    rebate = tax
    tax_payable = 0
else:
    rebate = 0
    tax_payable = tax

cess = tax_payable * 0.04
total_tax = tax_payable + cess

print("\n")
print("Taxable Income           :", taxable_income)
print("Section 87A Rebate       :", rebate)
print("Tax After Rebate         :", tax_payable)
print("Health & Education Cess  :", cess)
print("Total Tax Payable        :", total_tax)

