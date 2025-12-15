
def get_non_empty_string(message):
    while True:
        value = input(message).strip()
        if value == "":
            print("This field cannot be empty. Try again.")
        else:
            return value


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


def compute_annual_gross(monthly_salary):
    return monthly_salary * 12


def compute_taxable_income(annual_gross):
    STANDARD_DEDUCTION = 50000
    taxable = annual_gross - STANDARD_DEDUCTION
    return max(taxable, 0)


def compute_tax_new_regime(taxable_income):

    tax = 0

    # New regime slabs
    if taxable_income <= 300000:
        tax = 0

    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05

    elif taxable_income <= 900000:
        tax = (300000 * 0.05) + (taxable_income - 600000) * 0.10

    elif taxable_income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15

    elif taxable_income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20

    else:
        tax = ((300000 * 0.05) +
               (300000 * 0.10) +
               (300000 * 0.15) +
               (300000 * 0.20) +
               (taxable_income - 1500000) * 0.30)

    # Section 87A rebate
    if taxable_income <= 700000:
        rebate = tax
        tax_payable = 0
    else:
        rebate = 0
        tax_payable = tax

    cess = tax_payable * 0.04
    total_tax = tax_payable + cess

    return tax, rebate, cess, total_tax


def generate_report(name, emp_id, monthly_salary):

    annual_gross = compute_annual_gross(monthly_salary)
    taxable_income = compute_taxable_income(annual_gross)

    tax, rebate, cess, total_tax = compute_tax_new_regime(taxable_income)

    print("\nEmployee Tax Report")
    print("-------------------------------------")
    print("Name                   :", name)
    print("Employee ID            :", emp_id)
    print("Gross Monthly Salary   : ₹", monthly_salary)
    print("Annual Gross Salary    : ₹", annual_gross)
    print("Taxable Income         : ₹", taxable_income)
    print("-------------------------------------")
    print("Tax Before Rebate      : ₹", tax)
    print("Section 87A Rebate     : ₹", rebate)
    print("Tax After Rebate       : ₹", tax - rebate)
    print("Cess (4%)              : ₹", cess)
    print("Total Tax Payable      : ₹", total_tax)
    print("-------------------------------------")



print("Enter Employee Details")
print("-------------------------------------")

name = get_non_empty_string("Enter Name: ")
emp_id = get_non_empty_string("Enter Employee ID: ")
monthly_salary = get_positive_number("Enter Monthly Gross Salary (₹): ")

generate_report(name, emp_id, monthly_salary)
