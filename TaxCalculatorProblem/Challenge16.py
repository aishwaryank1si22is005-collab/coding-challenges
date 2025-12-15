import re

# -------------------------------------------------------------
# VALIDATION FUNCTIONS
# -------------------------------------------------------------

def get_valid_name(message):
    """Name: non-empty, alphabets only, max 50 characters"""
    while True:
        name = input(message).strip()

        if name == "":
            print("❌ Name cannot be empty. Please enter again.")
            continue
        
        if len(name) > 50:
            print("❌ Name cannot exceed 50 characters.")
            continue
        
        if not re.match(r"^[A-Za-z ]+$", name):
            print("❌ Name must contain alphabets and spaces only.")
            continue

        return name


def get_valid_empid(message):
    """EmpID: Alphanumeric, length 5–10"""
    while True:
        emp_id = input(message).strip()

        if not (5 <= len(emp_id) <= 10):
            print("❌ Employee ID must be 5–10 characters.")
            continue
        
        if not emp_id.isalnum():
            print("❌ Employee ID must contain alphabets and numbers only.")
            continue

        return emp_id


def get_valid_salary(message):
    """Salary inputs: Positive, max ₹1,00,00,000"""
    MAX_LIMIT = 10000000  # 1 crore

    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("❌ Value cannot be negative.")
                continue

            if value == 0:
                print("❌ Value cannot be zero. Enter a positive number.")
                continue

            if value > MAX_LIMIT:
                print("❌ Value exceeds allowed max limit (₹1,00,00,000).")
                continue

            return value
        except ValueError:
            print("❌ Invalid input. Enter a valid number.")


def get_valid_bonus(message):
    """Bonus percentage: must be between 0 and 100"""
    while True:
        try:
            value = float(input(message))

            if not (0 <= value <= 100):
                print("❌ Bonus % must be in the range 0–100.")
                continue

            return value
        
        except ValueError:
            print("❌ Invalid input. Enter a numeric value.")




print("\n===== Employee Input Validation =====")

name = get_valid_name("Enter Employee Name: ")
emp_id = get_valid_empid("Enter Employee ID: ")

basic_salary = get_valid_salary("Enter Basic Salary: ₹ ")
special_allowances = get_valid_salary("Enter Special Allowances: ₹ ")
bonus_percent = get_valid_bonus("Enter Bonus Percentage (0–100): ")




gross_monthly_salary = basic_salary + special_allowances + (basic_salary * bonus_percent / 100)
annual_gross_salary = gross_monthly_salary * 12


if gross_monthly_salary <= 0:
    print("\n❌ ERROR: Gross monthly salary must be greater than zero.")
else:
    print("\n✔ Gross salary validation successful.")


if annual_gross_salary > 50000000:  # 5 crore limit for sanity
    print("❌ ERROR: Annual gross salary unrealistic. Please recheck inputs.")
else:
    print("✔ Annual salary within realistic limits.")




print("Employee Name           :", name)
print("Employee ID             :", emp_id)
print("Basic Salary            : ₹", basic_salary)
print("Special Allowances      : ₹", special_allowances)
print("Bonus Percentage        :", bonus_percent, "%")
print("Gross Monthly Salary    : ₹", gross_monthly_salary)
print("Annual Gross Salary     : ₹", annual_gross_salary)

