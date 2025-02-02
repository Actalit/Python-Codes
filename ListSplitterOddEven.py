L = [10, -5, 7, -2, 3, 8, -9, 15, 0]

L1 = []
L2 = []

for num in L:
    if num > 0:
        L1.append(num)
    if num % 2 != 0:
        L2.append(num)

print(f"L1 (positive numbers): {L1}")
print(f"L2 (odd numbers): {L2}")