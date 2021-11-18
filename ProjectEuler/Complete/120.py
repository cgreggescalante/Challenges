# Square Remainders

total = 0

for a in range(3, 1001):
    if a % 2 == 0:
        total += a * (a - 2)
    else:
        total += a * (a - 1)

print(total)
