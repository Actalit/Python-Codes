n = int(input("Enter number of elements for the list: "))
L = []
L1=[]
L2=[]
for i in range(n):
    val = int(input("Enter value: "))
    L.append(val)
for j in range(len(L)//2):
    L1.append(L[j])
for k in range(len(L)//2,len(L)):
    L2.append(L[k])
print(L2+L1)