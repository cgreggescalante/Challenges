# Totient Chains
from math import gcd

import primesieve
from tqdm import tqdm

from Utilities.Factoring import prime_factors


def tot_chain(n):
    if n in known:
        return known[n]

    # factors = prime_factors(n)
    #
    # sieve = {i for i in range(1, n)}
    # for f in factors:
    #     i = f
    #     while i < n:
    #         if i in sieve:
    #             sieve.remove(i)
    #         i += f
    rel_prime = set()
    if n not in known_t:
        c = 0
        for k in range(1, n + 1):
            if gcd(n, k) == 1:
                c += 1
                if k > 1 and k in known_t:
                    rel_prime.add(k)
    # print(n, c)
        known_t[n] = c
        v = 1 + tot_chain(c)
    else:
        # print("used")
        v = known_t[n]

    known[n] = v
    # for m in rel_prime:
    #     if n * m < target:
    #         known_t[n * m] = known_t[n] * known_t[m]
    return v


target = 40000000
target_length = 25
primes = primesieve.primes(target)

known = {1: 1, 2: 2}
known_t = {}

total = 0
for p in tqdm(primes[:2000]):
    c = tot_chain(p)
    if c == target_length:
        total += p

print(total)
print(known_t)
