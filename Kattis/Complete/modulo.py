# Modulo

n = {}

for _ in range(10):
    x = int(input())
    n[x % 42] = 0

print(len(n))
