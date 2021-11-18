# Ordered Radicals
from Utilities.Factoring import prime_factors


def rad(x):
    factors = prime_factors(x)

    a = 1
    for factor in factors:
        a *= factor

    return a


prime_factors(1)
print("Initialized Primes\n")

radicals = {}

for n in range(1, 100001):
    radicals[n] = rad(n)

ordered = sorted(radicals.keys(), key=lambda x: radicals[x])

print(ordered[9999])
