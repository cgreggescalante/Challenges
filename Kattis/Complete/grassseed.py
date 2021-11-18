# Grass Seed Inc.

C = float(input())
L = int(input())

t = 0

for _ in range(L):
    w, l = map(float, input().split())
    t += w * l

print(t * C)
