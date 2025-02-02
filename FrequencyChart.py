s = input("Enter string: ")
u=0
l=0
a=0
n=0
for i in s:
    if i.isalpha():
        a+=1
        if i.islower():
            l+=1
        elif i.isupper():
            u+=1
    elif i.isdigit():
        n+=1
print(f'''Alphabets-{a}
      Numbers-{n}
      UpperCase-{u}
      Lowercase-{l}''')