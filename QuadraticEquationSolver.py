import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b**2-4*a*c
x1=(-b+math.sqrt(d))/(2*a)
x2=(-b-math.sqrt(d))/(2*a)
if d>0:
    print(f'''Solution 1 is: {x1}
Solution 2 is {x2}''')

if d==0:
    print(f'''Solution 1 is: {x1}''' or '''
Solution 2 is {x2}''')

if d<0:
    print("No real solution.")