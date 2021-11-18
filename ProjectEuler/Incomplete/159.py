# Digital Root Sums of Factorizations
import primesieve
from tqdm import tqdm

known = {}

def get_values_cum(target, product=1, value=2):


def get_values(target, product=1, value=2):
    if target == product:
        return [[]]

    results = []
    for i in range(value, target // product + 1):
        if target % i == 0:
            for r in get_values(target, product * i, i):
                results.append([i] + r)
    return results


def digital_root(n):
    s = sum(map(int, [a for a in str(n)]))
    if s >= 10:
        return digital_root(str(s))
    return s


def digital_sum(arr):
    s = 0
    for a in arr:
        s += digital_root(a)
    return s


def mdrs(n):
    facts = get_values(n)
    m = 0
    for f in facts:
        s = digital_sum(f)
        if s > m:
            m = s
    return m


primes = primesieve.primes(10**6 + 1000)
prime_check = {}
for p in primes:
    prime_check[p] = 0

s = 0
for n in tqdm(range(2, 10000)):
    try:
        a = prime_check[n]
        s += digital_root(n)
    except KeyError:
        s += mdrs(n)
print(s)
