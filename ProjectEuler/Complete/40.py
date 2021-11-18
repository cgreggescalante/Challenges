c = ''
count = 1
while len(c) < 1000020:
    c += str(count)
    count += 1

indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]

total = 1
for i in indexes:
    total *= int(c[i-1])

print(total)