# Chinese Remainder Theorem (non-relatively prime moduli)
from math import gcd

t = int(input())

for _ in range(t):
    a, n, b, m = map(int, input().split())
    k = (n * m) // gcd(n, m)
    found = False
    if n > m:
        start = a
        step = n
        ca = b
        cb = m
    else:
        start = b
        step = m
        ca = a
        cb = n
    for x in range(start, k, step):
        if (x - ca) % cb == 0:
            print(x, k)
            found = True
            break
    if not found:
        print("no solution")
