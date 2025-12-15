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



annual_gross_salary = get_positive_number("Enter Annual Gross Salary: ")
total_tax_payable = get_positive_number("Enter Total Tax Payable (including cess): ")

while True:
        
            if annual_gross_salary<= total_tax_payable:
                print("Gross salary should be greater than the tax")
                annual_gross_salary = get_positive_number("Enter Annual Gross Salary: ")
                total_tax_payable = get_positive_number("Enter Total Tax Payable (including cess): ")
            else:
                break
        

annual_net_salary = annual_gross_salary - total_tax_payable



print("Annual Gross Salary  :", annual_gross_salary)
print("Total Tax Payable    :", total_tax_payable)
print("Annual Net Salary    :", annual_net_salary)

