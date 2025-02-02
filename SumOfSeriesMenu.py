import math

x = int(input("Enter number: "))
n= int(input("Enter range: "))
choice = input("1: For the series  1+x^2+x^3....\n2: For the series x-x2/3! + x-x3/5! + x-x4/7!. . . .\n:: ")
if choice=='1':
    result=1
    for i in range(2,n+1):
        result+=x**i
    print(result)
elif choice=="2":
    result = 0
    fact=3
    for i in range(2,n+1):
        result+=(x-x**i)/math.factorial(fact)
        fact+=2
    print(result)
else:
    print("Invalid choice.")