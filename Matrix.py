L=[]
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
for i in range(rows):
    L1=[]
    for j in range(columns):
        val = input("Enter element: ")
        L1.append(val)
    L.append(L1)

for i in range(rows):
    for j in range(columns):
        print(L[i][j],end=' ')
    print()
    