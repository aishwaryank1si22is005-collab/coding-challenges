while True:
    try:
        n=int(input("Enter the number of rows:"))
        if n>0:
            break
    except ValueError:
        print("Invalid Input")

for i in range(n):
    for j in range(i):
        print("*",end="")
    print()