names = tuple(input("Enter names separated by spaces: ").split())
result = [name for name in names if len(name) > 1 and (name[1] == 'A' or name[1] == 'a')]
print("Names whose second character is 'A' or 'a':", result)
