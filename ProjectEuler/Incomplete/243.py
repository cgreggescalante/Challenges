# Resilience
from math import gcd, log


def R(d):
    c = 0
    if d % 2 == 0:
        for n in range(1, d, 2):
            if gcd(n, d) == 1:
                c += 1
    else:
        for n in range(1, d):
            if gcd(n, d) == 1:
                c += 1

    return c / (d - 1)


MAXN = 10 ** 18


# Generates a list of the first primes (with product > MAXN).
def gen_primes():
    primes = []
    primes_product = 1
    for n in range(2, 10 ** 10):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
        if is_prime:
            primes.append(n)
            primes_product *= n
            if primes_product > MAXN: break
    return primes


# Generates a list of the hcn <= MAXN.
def gen_hcn():
    primes = gen_primes()
    hcn = [(1, 1, [])]
    for i in range(len(primes)):
        new_hcn = []
        for el in hcn:
            new_hcn.append(el)
            if len(el[2]) < i: continue
            e_max = el[2][i - 1] if i >= 1 else int(log(MAXN, 2))
            for e in range(1, e_max + 1):
                n = el[0]
                div = el[1]
                exponents = el[2].copy()
                n *= pow(primes[i], e)
                div *= e + 1
                exponents.append(e)
                if n > MAXN: break
                new_hcn.append((n, div, exponents))
        new_hcn.sort()
        hcn = [(1, 1, [])]
        for el in new_hcn:
            if el[1] > hcn[-1][1]: hcn.append(el)
    return hcn


threshold = 15499 / 94744
low = 1
print("Target :", threshold)
a = 120

# while True:
#     d = a + a * 1000
#     r = R(d)
#     if r < threshold:
#         print(r, d)
#         break
#     elif r < low:
#         print(r, d)
#         low = r
#     a += 10
hcn = gen_hcn()

for h in hcn[50:]:
    print(h[0])
    r = R(h[0])
    if r < threshold:
        print(r)
        break
    elif r < low:
        print(r)
        low = r
