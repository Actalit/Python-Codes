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

# Finding sum of each row
row_sums = []
for i in range(r):
    row_sum = sum(L[i])
    row_sums.append(row_sum)

# Finding sum of each column
col_sums = [0] * c
for j in range(c):
    col_sum = 0
    for i in range(r):
        col_sum += L[i][j]
    col_sums[j] = col_sum


print("Sum of each row:", row_sums)
print("Sum of each column:", col_sums)
