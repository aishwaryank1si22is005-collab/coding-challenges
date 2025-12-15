#Function to get the positive inputs only
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


name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic_salary = get_positive_number("Enter Basic Monthly Salary: ")
special_allowances = get_positive_number("Enter Special Allowances (Monthly): ")
bonus_percentage = get_positive_number("Enter Annual Bonus Percentage: ")

gross_monthly_salary = basic_salary + special_allowances
annual_salary_before_bonus = gross_monthly_salary * 12
bonus_amount = (bonus_percentage / 100) * annual_salary_before_bonus
annual_gross_salary = annual_salary_before_bonus + bonus_amount


print("Employee Name           :", name)
print("Employee ID             :", emp_id)
print("Gross Monthly Salary    :", gross_monthly_salary)
print("Annual Gross Salary     :", annual_gross_salary)

