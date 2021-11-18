# Pandigital Prime
from Utilities.EratosthenesSieve import primes_in_range


def is_permutation(a):
    b = [d for d in range(1, len(str(a))+1)]
    for x in [int(d) for d in str(a)]:
        if x in b:
            b.remove(x)
        else:
            return False
    return len(b) == 0


n = 1
largest = 0

while True:
    primes = primes_in_range(10**n)

    for p in primes:
        if is_permutation(p):
            print(p)

    n += 1