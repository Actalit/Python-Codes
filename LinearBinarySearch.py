L = []
r = int(input("Rows: "))
c = int(input("Columns: "))

for i in range(r):
    L1 = []
    for j in range(c):
        ele = int(input(f"Enter element for position ({i+1},{j+1}): "))
        L1.append(ele)
    L.append(L1)

# Printing the matrix
print("\nThe Matrix is:")
for i in range(r):
    for j in range(c):
        print(L[i][j], end=" ")
    print()

# Linear Search
target = int(input("\nEnter element to search using Linear Search: "))
found = False
for i in range(r):
    for j in range(c):
        if L[i][j] == target:
            print(f"Linear Search: Element found at position ({i+1},{j+1})")
            found = True
            break
    if found:
        break
if not found:
    print("Linear Search: Element not found.")

# Binary Search (requires a sorted list)
L_flat = [L[i][j] for i in range(r) for j in range(c)]  # Flatten the matrix
L_flat.sort()

target = int(input("\nEnter element to search using Binary Search: "))
low = 0
high = len(L_flat) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if L_flat[mid] == target:
        print(f"Binary Search: Element found at index {mid}")
        found = True
        break
    elif L_flat[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Binary Search: Element not found.")
