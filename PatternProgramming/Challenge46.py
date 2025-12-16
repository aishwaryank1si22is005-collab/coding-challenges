while True:
    try:
        num = int(input("Enter number: "))
        break
    except ValueError:
        print("Invalid input")

rev = 0
temp = abs(num)

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if num < 0:
    rev = -rev

print("Reversed Number:", rev)
