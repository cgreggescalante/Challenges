# Tetration
import math


def tet(a, target):
    n = a
    i = 0
    prev = n
    while True:
        n = a ** n
        i += 1
        if round(prev, 8) == round(n, 8):
            return round(n, 8)
        prev = n


c = .1
d = 1
target = 2.718

while True:
    c += 1 / 10 ** d
    t = tet(c, target)
    print(c, t, d)
    if t > target:
        c -= 1 / 10 ** d
        d += 1
    elif round(c, 3) == 1.4:
        d += 1
    if abs(t - target) < 10 ** -5:
        break

print(round(c, 6))
