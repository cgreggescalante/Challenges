# Square Root Digital Expansion
from decimal import *
from math import sqrt

getcontext().prec = 200


def sum_digits(n):
    s = str(n)[2:]
    total = 0
    for i in range(99):
        total += int(s[i])
    return total + int(n)


total = 0
for n in range(100):
    rt_n = sqrt(n)
    if rt_n != int(rt_n):
        d = Decimal(n) ** Decimal(.5)
        total += sum_digits(d)

print(total)
