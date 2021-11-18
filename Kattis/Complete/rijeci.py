# Rijeci

a = 1
b = 0

n = int(input())

for _ in range(n):
    na = b
    nb = a + b
    a, b, = na, nb

print(a, b)
