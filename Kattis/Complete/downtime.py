# Disastrous Downtime
from math import ceil

n, k = map(int, input().split())

m = 0

s = []

for _ in range(n):
    t = int(input())
    while s != [] and s[0] + 1000 <= t:
        s.pop(0)
    s.append(t)
    if len(s) > m:
        m = len(s)

print(ceil(m / k))
