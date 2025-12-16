while True:
    try:
        n = int(input("Enter number of rows: "))
        if n > 0:
            break
        print("Rows must be positive")
    except ValueError:
        print("Invalid input")

for i in range(n):
    for j in range(5):
        print("*", end="")
    print()
