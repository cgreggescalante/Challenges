# Licence Plates
from math import gamma
from decimal import *


getcontext().prec = 10000

prob = .001

n = Decimal(46.22415454)
steps = 0
while n < 50:
    a = gamma(n)
    b = gamma(n - 2) * 2
    c = gamma(n) / (2 * gamma(n - 2))
    print(steps, n, prob * c)
    if a >= b * 1000:
        break
    n += Decimal(.000000001)
    steps += 1

# result should be between 45 and 46
