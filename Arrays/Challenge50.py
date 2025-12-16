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
odd_count = 0
even_count = 0

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Array elements:", arr)
print("Odd numbers count:", odd_count)
print("Even numbers count:", even_count)
