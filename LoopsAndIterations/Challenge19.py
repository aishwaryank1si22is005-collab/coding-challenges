while True:
    try:
        n = int(input("Enter N: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

count = 0
num = 2

while count < n:
    print(num * num, end=" ")
    num += 2
    count += 1
