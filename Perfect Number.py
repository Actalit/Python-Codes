value = int(input("Enter number: "))
Sum=0
for i in range(1,value):
    if value%i==0:
        Sum+=i
if value==Sum:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")