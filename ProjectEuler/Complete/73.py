# Counting Fractions in a Range
import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499]


def prime_factors(x):
    factors = []

    root_x = math.sqrt(x) + 1

    for p in primes:
        if p > root_x:
            break
        if x % p == 0:
            factors.append(p)
            x /= p
        while x % p == 0:
            x /= p

    for i in range(primes[-1] + 2, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            factors.append(i)

        while x % i == 0:
            x /= i

    if x > 2 and x not in factors:
        factors.append(x)

    return factors


def factor(x):
    factors = []

    for i in range(2, x):
        if x % i == 0:
            factors.append(i)

    return factors


def overlap(a, b):
    # Use of hybrid method
    temp = set(b)
    lst3 = [value for value in a if value in temp]
    return len(lst3) > 0


fractions = []

for d in range(4, 12001):
    print(d)
    facts = prime_factors(d)
    step = 1
    start = 0
    if d % 2 == 0:
        step = 2
    if int(d / 3) % 2 == 0:
        start = 1
    for n in range(int(d / 3) + start, int(d / 2) + 1, step):
        if (1.0 / 3.0) < (n / (d + 0.0)) < .5:
            if not overlap(facts, prime_factors(n)):
                fractions.append([n, d])

print(len(fractions))
