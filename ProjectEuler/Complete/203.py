# Squarefree Binomial Coefficients
from math import factorial

from Utilities.EratosthenesSieve import primes_in_range


def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


primes = primes_in_range(10**7)


distinct_pascals = {}

for n in range(51):
    for r in range(n+1):
        distinct_pascals[ncr(n, r)] = 0

s = 0

for pascal in distinct_pascals:
    squarefree = True
    for prime in primes:
        p2 = prime * prime
        if p2 > pascal:
            break
        if pascal % p2 == 0:
            squarefree = False
            break
    if squarefree:
        s += pascal

print(s)
