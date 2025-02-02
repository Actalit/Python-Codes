S1 = float(input("Enter marks: "))
S2 = float(input("Enter marks: "))
S3 = float(input("Enter marks: "))
S4 = float(input("Enter marks: "))
S5 = float(input("Enter marks: "))
total = int(input("Enter how many marks the exams were out of: "))
percentage = (S1+S2+S3+S4+S5)/(total*5)*100

if percentage>=60:
    print(f"First Division {percentage}%.")
elif percentage>=45:
    print(f"Second Division {percentage}%.")
elif percentage>=33:
    print(f"Third Division {percentage}%.")
else:
    print(f"Failed {percentage}%.")