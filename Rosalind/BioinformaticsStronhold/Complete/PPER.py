# Partial Permutations

n = 92
k = 9

t = 1

for i in range(n, n - k, -1):
    t *= i
    t %= 1000000

print(t)