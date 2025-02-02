str1 = input("Enter string: ")
word = input("Enter word you're looking for: ")
str1.lower()
word.lower()
if word in str1:
    print("It is present in the string.")
else:
    print("Given word does not exist in string.")