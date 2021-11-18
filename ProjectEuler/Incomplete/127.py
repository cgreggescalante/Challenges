# ABC-Hits
from math import gcd

from tqdm import tqdm

from Utilities.Factoring import prime_factors


def rad(x, y, z):
    """Return the product of all prime factors of x * y * z.

    >>> rad(5, 27, 32)
    30
    >>> rad(21, 6, 4)
    42
    """
    factors = set(prime_factors(x))
    factors.update(set(prime_factors(y)))
    factors.update(set(prime_factors(z)))
    product = 1
    for f in factors:
        product *= f

    return product


if __name__ == '__main__':
    total = 0
    target = 1000
    count = 0

    for c in range(2, target):
        sieve = set(range(2, c))
        for f in prime_factors(c):
            i = f
            while i < c:
                if i in sieve:
                    sieve.remove(i)
                i += f
        if len(sieve) < 2:
            continue

        for a in sieve:
            b = c - a
            if b <= a or b not in sieve:
                continue
            if gcd(a, b) != 1:
                continue
            if rad(a, b, c) < c:
                print(a, b, c)
                total += c
                count += 1

    print(total)
    print(count)
