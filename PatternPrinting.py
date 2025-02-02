choice=input("1-Alphabet Pattern\n2-Numerical Pattern\n::")
if choice=="1":
    rows=4
    alphabet = ord('A')
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(alphabet), end="\t")
            alphabet += 1
        print()
elif choice=="2":
    rows=4
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(j,end="\t")
        print()
        