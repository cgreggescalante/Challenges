# Odd period square roots
from math import sqrt, gcd


def period(n, m=None, target=None, d=None):
    if m is None:
        m = int(sqrt(n))
        d = n - m ** 2
    else:
        a = int(sqrt((sqrt(n) + m) / d))
        print(a)
        c = m - a * d
        d = (n - c ** 2) // d
        m = -c
    if target is None:
        target = sqrt(n) - int(sqrt(n))

    print(f"n:{n}, m:{m}, d:{d}")

    x = (sqrt(n) + m) / d
    if x == target:
        return []

    return [x].extend(period(n, m, target, d))


print(period(14))
