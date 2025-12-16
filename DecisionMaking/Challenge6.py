while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
