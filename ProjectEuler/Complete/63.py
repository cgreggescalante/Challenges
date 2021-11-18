count = 0

for n in range(22):
    for b in range(1, 10):
        if len(str(b ** n)) == n:
            print(str(b) + '^' + str(n))
            count += 1
        elif len(str(b ** n)) > n:
            break

print(count)