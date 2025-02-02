n=int(input("Enter number: "))
a=1
b=0
sum=a+b
count=0
while count<n:
	a=b
	b=sum
	sum=a+b
	count+=1
print(sum)