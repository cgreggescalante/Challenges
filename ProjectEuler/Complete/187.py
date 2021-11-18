# Semiprimes
import primesieve
from tqdm import tqdm

target = 10**8

primes = primesieve.primes(target)

check = {}

for i in tqdm(range(len(primes))):
    for j in range(i, len(primes)):
        sp = primes[i] * primes[j]
        if sp < target:
            check[sp] = 0
        else:
            break

print(len(check.keys()))
