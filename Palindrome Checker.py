choice = int(input('''Enter which method you would like to use to check for a palindrome
               1-Slicing
               2-For loop for strings
               3-For loop for integers
               --: '''))
if choice==1:
    value=input("Enter the string to be checked: ")
    value1=value[::-1]
    if value==value1:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

if choice==2:
    value=input("Enter the string to be checked: ")
    rev=''
    for i in range(len(value)-1,-1,-1):
        rev+=value[i]
    if rev==value:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

if choice==3:
    value=int(input("Enter number to be checked: "))
    rev=0
    new_value=value
    while new_value>0:
        digit=new_value%10
        rev=rev*10+digit
        new_value=new_value//10
    if rev==value:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")