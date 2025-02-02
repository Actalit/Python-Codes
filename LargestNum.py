num1=float(input("Enter number: "))
num2=float(input("Enter number: "))
num3=float(input("Enter number: "))
if num1>num2>num3 or num1>num3>num2:
    print(f"{num1} is the greatest.")
elif num2>num1>num3 or num2>num3>num1:
    print(f"{num2} is the greatest.")
else:
    print(f"{num3} is the greatest.")