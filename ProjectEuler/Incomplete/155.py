# Counting Capacitor Circuits

from decimal import *

getcontext().prec = 100

known = {1: [60]}

r_val = 10


def series(n):
    if n in known:
        return known[n]

    options = set()

    for i in range(n+1):
        if i != n:
            options.add(Decimal(1 / (1 / 60 * (n - i))))
        if i > 1:
            ps = parallel(i)
            for p in ps:
                options.add(Decimal(1 / (Decimal(1 / 60 * (n - i)) + (1 / p))))

    known[n] = sorted(options)
    return options


def parallel(n):
    # print(n)
    options = set()
    for i in range(1, int(n / 2 + 1)):
        # print(i, n - i)
        a = series(i)
        b = series(n - i)
        for x in a:
            for y in b:
                options.add(Decimal(x + y))
    return options


for i in range(1, 19):
    a = sorted(series(i))
    print(i, len(a))

