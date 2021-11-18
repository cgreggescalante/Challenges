# Prime Summations
import primesieve

primes = primesieve.primes(10**6)


def prime_sum(n, top=10**10):
    if n == 1:
        return 0
    elif n < 4:
        return 1

    c = 0

    if n % 2 == 0:
        c += 1

    for p in primes[1:]:
        if p > n or p > top:
            break
        c += prime_sum(n - p, p)

    return c


for i in range(100):
    a = prime_sum(i)
    if a > 5000:
        print(i, a)
        break

