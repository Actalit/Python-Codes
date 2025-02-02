s1 = int(input("Enter side: "))
s2 = int(input("Enter side: "))
s3 = int(input("Enter side: "))
if s1==s2==s3:
    print("It is equilateral.")
elif s1!=s2!=s3!=s1:
    print("It is scalene.")
else:
    print("It is isosceles.")