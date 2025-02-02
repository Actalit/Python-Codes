L = [10, 3, 7, 5, 20, 1]

largest = L[0]

for num in L:
    if num > largest:
        largest = num

print(f"The largest element in the list is: {largest}")
