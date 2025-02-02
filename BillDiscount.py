bill = float(input("Enter bill amount: "))
if bill>=20000:
    print("Net payable amount-",bill-((bill/100)*15))
elif bill>=15000:
    print("Net payable amount-",bill-((bill/100)*10))
elif bill>=10000:
    print("Net payable amount-",bill-((bill/100)*5))
else:
    print("Net payable amount-",bill)