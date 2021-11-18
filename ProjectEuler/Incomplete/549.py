# Divisibility of factorials
import primesieve

from Utilities.Factoring import prime_factors

primes = set(primesieve.primes(10**8 + 1))


def smallest_m(n):
    if n in primes:
        return n
    factors = prime_factors(n, allow_repeats=True)
    d = {f: factors.count(f) for f in set(factors)}
    divisors = set()
    for k, v in d.items():
        divisors.add(k * v)
    return max(divisors)


target = 100
total = 0
for n in range(2, target + 1):
    s = smallest_m(n)
    print(n, s)
    total += s

print(total)
