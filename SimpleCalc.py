num1=float(input("Enter number: "))
choice= int(input("Choose operation:\nMultiplication-1\nDivision-2\nAddition-3\nSubtraction-4\n::"))
num2=float(input("Enter number: "))

if choice==1:
    print(num1*num2)
elif choice==2:
    print(num1/num2)
elif choice==3:
    print(num1+num2)
elif choice==4:
    print(num1-num2)
else:
    print("Invalid Choice.")