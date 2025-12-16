while True:
    try:
        n = int(input("Enter number of terms: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

num = 1
count = 0

while count < n:
    square = num * num
    print(square, end=" ")
    num += 1
    count += 1
