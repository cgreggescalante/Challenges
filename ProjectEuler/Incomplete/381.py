import primesieve
from tqdm import tqdm


def modular_fact(n, p):
    t = 1
    for i in range(2, n):
        t *= i
        t %= p
    return t


def S(p, a):
    t = 0
    for i in range(p, p + 5):
        t += a
        a *= 1 if i == 0 else i
        a %= (p + 5)
    return t % (p + 5)


total = 0
target = 100
prime_check = {}
for p in primesieve.primes(target):
    prime_check[p] = 0

fact = 1

for p in range(target):
    if p:
        fact *= p
    try:
        x = prime_check[p + 5]
        s = S(p, fact + 0)
        print(p+5, s)
        total += s
    except KeyError:
        pass

print(total)
