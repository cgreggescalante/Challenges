import primesieve

primes = primesieve.primes(10**7)


def is_prime(n, warn=False):
    if n < 2:
        return False
    s = n ** .5
    for i in primes:
        if i > s:
            return True
        if n % i == 0:
            return False

    if warn:
        print("Exceeded max stored prime :", primes[-1])
        print("Current configuration applicable for inputs up to", primes[-1]**2)
    for i in range(primes[-1] + 2, int(n ** .5) + 1, 2):
        if n % i == 0:
            return False
    return True
