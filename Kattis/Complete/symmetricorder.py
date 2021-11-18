# Symmetric Order
from math import ceil

s = 1
n = int(input())

while n > 0:
    print("SET", s)

    names = []
    for i in range(n):
        names.insert(ceil(i / 2), input())

    print('\n'.join(names))

    n = int(input())
    s += 1
