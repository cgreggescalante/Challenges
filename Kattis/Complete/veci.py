# Veci
from itertools import permutations

x = int(input())

perm = permutations(sorted([a for a in str(x)]))

found = False

for i in list(perm):
    c = int(''.join(i))
    if c > x:
        print(c)
        found = True
        break

if not found:
    print(0)
