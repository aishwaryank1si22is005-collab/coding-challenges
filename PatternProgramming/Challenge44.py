while True:
    try:
        n = int(input("Enter number of terms: "))
        if n > 0:
            break
    except ValueError:
        print("Invalid input")

sign=1
num=1
for i in range(1,n+1):
    print(num*sign , end=" ")
    num=num+4
    sign*=-1
