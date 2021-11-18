# Grandpa Bernie
from collections import defaultdict

n = int(input())

d = defaultdict(lambda: [])

for _ in range(n):
    s, y = input().split()
    d[s].append(int(y))

for i in d:
    d[i] = sorted(d[i])

q = int(input())

for _ in range(q):
    s, k = input().split()
    k = int(k)

    print(d[s][k-1])
