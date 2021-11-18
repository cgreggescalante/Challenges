# Enumerating Gene Orders
from itertools import permutations

n = 7

nums = ''.join([str(a) for a in range(1, n+1)])

perm = sorted(' '.join(c) for c in permutations(nums))

a = 1
for i in range(2, n+1):
    a *= i

print(a)
for p in perm:
    print(p)