# Prime Generator
# ID: 2
# Key: PRIME1
from math import sqrt

t = int(input())

for _ in range(t):
    m, n = map(int, input().split())

    primes = [i for i in range(2, int(sqrt(n))+1)]

    for i in range(len(primes)):
        if primes[i] == -1:
            continue
        for j in range(i+primes[i], len(primes), primes[i]):
            primes[j] = -1

    primes = [p for p in primes if p > 0]

    mark = [i for i in range(m, n+1)]

    for p in primes:
        start = m // p * p
        if start < m:
            start += p
        if start == p:
            start += p
        for i in range(start, n + 1, p):
            mark[i - m] = -1

    mark = [m for m in mark if m > 1]
    print('\n'.join(map(str, mark)))
