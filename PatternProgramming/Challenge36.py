while True:
    try:
        n = int(input("Enter number of rows: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

for i in range(n):
    for j in range(1, 6):
        print(j, end="")
    print()
