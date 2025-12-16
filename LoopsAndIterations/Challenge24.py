while True:
    try:
        n = int(input("Enter number of terms: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

a, b = 1, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
