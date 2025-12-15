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


annual_gross=get_positive_number("Enter the annual gross salary: ")
standard_deduction=50000
taxable_income=annual_gross-standard_deduction
print("Gross alary:", annual_gross)
print("Standard Deduction: ",standard_deduction)
print("Taxable Income: ",taxable_income)
