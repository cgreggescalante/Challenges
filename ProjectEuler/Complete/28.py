# Number Spiral Diagrams

total = 1

for x in range(3, 1002, 2):
    for i in range(0, 4):
        total += (x**2 - (i * (x - 1)))

print(total)
