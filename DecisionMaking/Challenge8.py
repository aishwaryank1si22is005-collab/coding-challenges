numbers = []

for i in range(1, 4):
    while True:
        try:
            value = float(input(f"Enter number {i}: "))
            numbers.append(value)
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
