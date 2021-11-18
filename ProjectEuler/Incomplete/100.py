# Arranged Probability
from math import sqrt
from decimal import *


getcontext().prec = 1000


def perc_r(b):
    a = Decimal(8 * b ** 2 - 8 * b + 1).sqrt()
    a -= 2 * b
    a += 1
    return a / 2


def R(b):
    a = sqrt(8 * b ** 2 - 8 * b + 1)
    a -= 2 * b
    a += 1
    return a / 2


for b in range(707106781186, 10**13):
    r = perc_r(b)
    if int(r) == r:
        print(b, int(r), b + int(r))
        if r + b > 10**12:
            break
