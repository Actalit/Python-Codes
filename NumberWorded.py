number_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
number = input("Enter a number: ")
words = []
for digit in number:
    if digit.isdigit():
        words.append(number_words[int(digit)])
result = " ".join(words)

print(f"The number in words is: {result}")
