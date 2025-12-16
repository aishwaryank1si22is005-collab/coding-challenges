while True:
    try:
        n = int(input("Enter number of terms: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

value = 1
increment = 1

for i in range(n):
    print(value, end=" ")
    increment += 1
    value += increment
