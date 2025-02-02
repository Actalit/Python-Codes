sale = int(input("Enter monthly sales: "))
if sale>500000:
    print("Your bonus this month is",sale/100*10)
else:
    print("Your bonus this month is",sale/100*5)
