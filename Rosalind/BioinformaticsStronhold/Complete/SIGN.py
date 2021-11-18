# Enumerating Oriented Gene Orderings
from itertools import permutations

n = 5

nums = [a for a in range(1, n+1)]

perm = permutations(nums, n)

t = 2**n
for i in range(2, n + 1):
    t *= i

print(t)

for i in perm:
    for k in range(2**len(i)):
        s = []
        b = '0' * (len(i) - len(bin(k)) + 2) + bin(k)[2:]
        for a in range(len(i)):
            if b[a] == '1':
                s.append(i[a])
            else:
                s.append(-i[a])
        print(' '.join([str(a) for a in s]))

