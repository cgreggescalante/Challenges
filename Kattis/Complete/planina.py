# Planina

N = int(input())

s = 2
for _ in range(N):
    s += s - 1

print(s * s)
