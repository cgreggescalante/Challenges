# Idempotents
import primesieve
from tqdm import tqdm

check = {}
for p in primesieve.primes(10**7):
    check[p] = 0


def m(n):
    for a in range(n-1, -1, -1):
        if a*a % n == a:
            return a


total = 0
for n in tqdm(range(1, 10**7 + 1)):
    try:
        x = check[n]
        total += 1
    except KeyError:
        total += m(n)

print(total)
