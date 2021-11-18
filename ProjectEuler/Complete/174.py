# Square Laminae Arrangements

counts = {}

for inner in range(1, 250001):
    i2 = inner * inner
    for outer in range(inner + 2, 250002, 2):
        t = outer ** 2 - i2
        if t > 1000000:
            break
        try:
            counts[t] += 1
        except KeyError:
            counts[t] = 1


total = 0

for key, value in counts.items():
    if value <= 10:
        total += 1

print(total)
