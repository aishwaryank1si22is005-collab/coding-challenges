while True:
    try:
        n = int(input("Enter number of rows: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()
