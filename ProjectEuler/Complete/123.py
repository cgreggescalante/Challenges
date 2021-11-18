# Prime Square Remainders
from Utilities.EratosthenesSieve import primes_in_range


def square_remainder(n):
    p = primes[n-1]
    p2 = p * p
    c = pow(p - 1, n, p2) + pow(p + 1, n, p2)

    return c % p2


primes = primes_in_range(10**7)

r = 0
t = 0
target = 10**10

while r <= target and t < 10**7:
    t += 1
    a = square_remainder(t)
    if a > r:
        r = a
        print(a / target, primes[t-1])

print(t, r)
