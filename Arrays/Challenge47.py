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

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

minimum = arr[0]

for value in arr:
    if value < minimum:
        minimum = value

print("Array elements:", arr)
print("Minimum value:", minimum)
