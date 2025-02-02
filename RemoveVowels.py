s = input("Enter string: ")
s2 = ''
vowels = 'aeiouAEIOU'
for i in s:
    if i in vowels:
        pass
    else:
        s2+=i
print(s2)