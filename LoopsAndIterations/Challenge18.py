while True:
    try:
        n = int(input("Enter N: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

for i in range(1, n + 1, 2):
    print(i, end=" ")
