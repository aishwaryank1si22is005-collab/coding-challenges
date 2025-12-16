while True:
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            print("n must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input. Enter an integer value.")

arr = []
total = 0

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)
    total += value

print("Array elements:", arr)
print("Sum of elements:", total)
