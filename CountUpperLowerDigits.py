string = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
digit_count = 0

for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1

print(f'''Uppercase letters: {uppercase_count}\nLowercase letters: {lowercase_count}\nDigits: {digit_count}''')
