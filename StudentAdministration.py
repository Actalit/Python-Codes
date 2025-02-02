students = []
while True:
    print("""
    Menu:
    1. Add new student
    2. Display students with marks > 85
    3. Delete a student record
    4. Update a student record
    5. Display all student records
    6. Exit
    """)
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    if choice == '1':
        roll_no = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        stream = input("Enter stream: ")
        marks = float(input("Enter marks: "))
        students.append({"roll_no": roll_no, "name": name, "stream": stream, "marks": marks})
        print("Student added successfully!")
    elif choice == '2':
        print("\nStudents with marks > 85:")
        found = False
        for student in students:
            if student["marks"] > 85:
                print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Stream: {student['stream']}, Marks: {student['marks']}")
                found = True
        if not found:
            print("No students with marks > 85.")
    elif choice == '3':
        roll_no = int(input("Enter roll number to delete: "))
        students = [student for student in students if student["roll_no"] != roll_no]
        print(f"Student with roll number {roll_no} deleted successfully.")
    elif choice == '4':
        roll_no = int(input("Enter roll number to update: "))
        found = False
        for student in students:
            if student["roll_no"] == roll_no:
                student["name"] = input("Enter new name: ")
                student["stream"] = input("Enter new stream: ")
                student["marks"] = float(input("Enter new marks: "))
                print("Student record updated successfully.")
                found = True
                break
        if not found:
            print(f"No student found with roll number {roll_no}.")
    elif choice == '5':
        print("\nList of all students:")
        for student in students:
            print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Stream: {student['stream']}, Marks: {student['marks']}")
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
