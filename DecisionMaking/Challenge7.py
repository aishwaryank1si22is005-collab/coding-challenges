while True:
    name = input("Enter Name: ").strip()
    if name.isalpha():
        break
    else:
        print("Invalid name. Enter alphabets only.")

while True:
    try:
        salary = float(input("Enter Annual Salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
        else:
            break
    except ValueError:
        print("Invalid salary. Enter numeric value.")

if salary > 300000:
    print(name, "must pay tax.")
else:
    print(name, "does not need to pay tax.")
