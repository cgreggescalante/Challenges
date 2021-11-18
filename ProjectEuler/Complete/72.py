# Counting Fractions

D = 1000000

options = [a for a in range(D+1)]
count = 0
for i in range(2, D+1):
    if options[i] == i:
        for j in range(i, D+1, i):
            options[j] = options[j] / i * (i - 1)
    count += options[i]

print(int(count))

