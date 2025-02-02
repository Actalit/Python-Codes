TEACHERS = {}
n = int(input("Enter the number of subjects: "))
for i in range(n):
    subject = input(f"Enter the name of subject {i + 1}: ")
    teacher = input(f"Enter the name of the teacher for {subject}: ")
    TEACHERS[subject] = teacher
print("\nOriginal TEACHERS dictionary:")
print(TEACHERS)
if "English" in TEACHERS:
    new_teacher = input("\nEnter the new teacher's name for English: ")
    TEACHERS["English"] = new_teacher
print("\nUpdated TEACHERS dictionary:")
print(TEACHERS)
