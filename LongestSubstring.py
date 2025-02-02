string1 = input("Enter a string: ")
list1 = string1.split()
greatest = list1[0]
for i in range(1,len(list1)):
    if len(list1[i])>len(greatest):
        greatest=list1[i]
print(greatest)