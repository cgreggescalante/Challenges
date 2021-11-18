from math import factorial

count = 0

for n in range(1, 101):
    for r in range(n+1):
        if (factorial(n))/(factorial(r) * factorial(n - r)) > 1000000:
            count += 1

print(count)