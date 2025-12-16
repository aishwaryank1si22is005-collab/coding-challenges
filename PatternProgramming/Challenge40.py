while True:
    try:
        n = int(input("Enter number of rows: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

a, b = 1, 1
count = 0

for i in range(1, n + 1):
    for j in range(i):
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()
