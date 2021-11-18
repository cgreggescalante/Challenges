# Investigating progressive numbers, n, which are also square

# n is divided by d
# the quotient and remainder are q and r
# d, q, r are consecutive positive integer terms in a geometric sequence

# n is progressive
# find sum of n under target where n is square

target = 10**12
total = 0

for a in range(1, int(target ** .5) + 1):
    n = a * a
    for d in range(1, n):
        q = n // d
        r = n % d
        if not r:
            continue
        arr = sorted([d, q, r])
        if arr[1] / arr[0] == arr[2] / arr[1]:
            print(n)
            total += n
            break

print(total)
