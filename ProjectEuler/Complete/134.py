from Utilities.EratosthenesSieve import primes_in_range

primes = primes_in_range(10**6+4)[2:]

total = 0

for i in range(len(primes) - 1):
    j = primes[i+1]
    p = len(str(primes[i]))

    matched = 2

    multiplier = 5
    if j % 2 == 1:
        multiplier = 10

    while j % 10 != primes[i] % 10:
        j += primes[i+1]

    while j % 10 ** p != primes[i]:
        while j % 10 ** matched != primes[i] % 10 ** matched:
            j += primes[i+1] * multiplier
        multiplier *= 10
        matched += 1

    total += j
    print(primes[i], primes[i + 1], j)

print(total)