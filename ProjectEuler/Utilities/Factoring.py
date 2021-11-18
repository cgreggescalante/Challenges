from math import sqrt

import primesieve

known_factors = {}
primes = []


def prime_factors(n, allow_repeats=False):
    global primes
    if not primes:
        primes = primesieve.primes(10**7)
    if allow_repeats:
        return all_prime_factors(n)
    if n < 1:
        return []

    factors = []

    sqrt_n = sqrt(n)

    for i in primes:
        if i > sqrt_n + 1:
            break
        if n % i == 0:
            factors.append(i)
        while n % i == 0:
            n /= i

    if n > 2 and int(n) not in factors:
        factors.append(int(n))

    return factors


def all_prime_factors(n):
    if n in known_factors:
        return known_factors[n]

    tr_n = sqrt(n)
    factors = []
    for i in primes:
        if i > tr_n + 1:
            break
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def divisors(n, inclusive=False):
    if n == 0:
        return []
    if n == 1:
        return [1]

    if inclusive:
        facts = [1, n]
    else:
        facts = [1]

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            facts.append(i)
            if n // i != i:
                facts.append(n // i)

    return facts
