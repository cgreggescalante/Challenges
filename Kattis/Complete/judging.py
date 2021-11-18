# Judging Troubles
from collections import defaultdict

n = int(input())

a = defaultdict(int)
b = defaultdict(int)

for _ in range(n):
    a[input()] += 1

for _ in range(n):
    b[input()] += 1

c = 0
for i in a:
    c += min([a[i], b[i]])

print(c)
