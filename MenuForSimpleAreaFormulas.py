while True:
    print("\nMenu:")
    print('''  1. Rectangle
    2. Square
    3. Circle
    4. Exit''')
    choice = int(input("Enter choice: "))
    if choice == 1:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(f"Area of rectangle: {l * w}")
    elif choice == 2:
        s = float(input("Enter side: "))
        print(f"Area of square: {s * s}")
    elif choice == 3:
        r = float(input("Enter radius: "))
        print(f"Area of circle: {3.14 * r * r}")
    elif choice == 4:
        break
    else:
        print("Invalid choice.")