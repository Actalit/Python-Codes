n = int(input("Enter the number of employees: "))
employee_data = {}
for i in range(n):
    name = input(f"Enter the name of employee {i + 1}: ")
    salary = float(input(f"Enter the salary of {name}: "))
    employee_data[name] = salary 
print("\nEmployee data stored in the dictionary:")
for name, salary in employee_data.items():
    print(f"Name: {name}, Salary: {salary}")
