s = input("Enter string: ")
s2 = ''
for i in range(len(s)):
    if i%2==0:
        s2+=s[i]
    else:
        s2+=s[i].upper()
print(s2)