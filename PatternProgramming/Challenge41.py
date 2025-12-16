while True:
    try:
        n = int(input("Enter number of rows: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

sign=1
num=1

for i in range(1, n + 1):
    for j in range(i):
        print(num*num*sign, end=" ")
        sign*=-1
        num+=1
    print()
