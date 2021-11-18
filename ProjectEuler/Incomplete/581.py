# 47-Smooth Triangular Numbers
import primesieve


def prod(d):
    total = 1
    for key, value in d.items():
        total *= key ** value
    return total


def is_tri(n):
    t = (8 * n + 1) ** .5
    return bool(t % 2)
    # sn = n ** .5
    # return int(sn) * int(sn + 1) == n * 2


def t(n):
    return n * (n + 1) / 2


d = {}
for a in primesieve.primes(50):
    d[a] = 0

i = 0
while i < 100:
    a = t(i)
    print(is_tri(a))
    i += 1
