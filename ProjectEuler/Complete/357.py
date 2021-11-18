# Prime Generating Integers
from tqdm import tqdm

from Utilities.EratosthenesSieve import primes_in_range
from Utilities.Factoring import divisors

primes = primes_in_range(10**8+1)
prime_check = {}
for p in primes:
    prime_check[p] = 0

total = 0
t = tqdm(range(len(primes)))
for p in primes:
    n = p - 1
    ds = divisors(n)

    works = True
    for d in ds[2:]:
        try:
            a = prime_check[d + n / d]
        except KeyError:
            works = False
            break

    if works:
        total += n
    t.update()

print(total)