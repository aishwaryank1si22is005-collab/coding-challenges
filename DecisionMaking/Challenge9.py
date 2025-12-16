while True:
    try:
        year = int(input("Enter year: "))
        if year <= 0:
            print("Year must be a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Enter a valid year.")

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
