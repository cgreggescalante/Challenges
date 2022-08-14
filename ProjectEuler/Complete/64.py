# Odd period square roots
from math import sqrt, gcd

count = 0

for n in range(2, 10001):
    sn = sqrt(n)

    if sn == int(sn):
        continue

    f = int(sn)
    c = f
    b = n - c**2

    start_c = c
    start_b = b

    i = 0
    while True:
        i += 1
        f = int((sn + c) / b)
        c -= b*f
        c *= -1
        m = b
        b = n - c**2
        g = gcd(m, b)
        b = b // g

        if c == start_c and b == start_b:
            if i % 2 == 1:
                count += 1

            break


print(count)
