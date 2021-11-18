# Largest integer divisible by two primes
import primesieve
from tqdm import tqdm

n = 10000000

primes = primesieve.primes(n)

total = 0

for a in tqdm(range(len(primes))):
    for b in range(a + 1, len(primes)):
        i = 1
        top = 0
        while primes[a] ** i * primes[b] <= n:
            j = 1
            while primes[a] ** i * primes[b] ** j <= n:
                if primes[a] ** i * primes[b] ** j > top:
                    top = primes[a] ** i * primes[b] ** j
                j += 1
            i += 1
        total += top

print(total)
