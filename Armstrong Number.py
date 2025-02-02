value = input("Enter number: ")
Sum=0
for i in value:
    Sum+= int(i)**len(value)
if Sum==int(value):
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number.") 