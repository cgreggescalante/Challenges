# Divisor Square Sum
from itertools import compress

from tqdm import tqdm


def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


primeslist = primes(int(64000000**0.5)+1)


def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primeslist:
        if p*p > n:
            break
        count = 0
        while not n % p:
            n //= p
            count += 1
        if count > 0:
            pf.append((p, count))
    if n > 1:
        pf.append((n, 1))
    return pf


def divisors(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1, e+1) for x in divs]
    return divs


total = 0

for n in tqdm(range(1, 64000000)):
    # divisors = [1, n]
    # start = 2
    # step = 1
    # if n % 2 == 1:
    #     start = 3
    #     step = 2
    # for i in range(start, int(n ** .5) + 1, step):
    #     if not n % i:
    #         divisors.append(i)
    #         divisors.append(n // i)

    t = sum([a * a for a in divisors(n)])

    t2 = t ** .5
    if int(t2) == t2:
        total += n

print(total)
