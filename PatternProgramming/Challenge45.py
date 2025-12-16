while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input")

whole = int(num)
fraction = num - whole

print("Whole Part:", whole)
print("Fractional Part:", fraction)
