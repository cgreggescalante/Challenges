# Tarifa

X = int(input())
N = int(input())

available = X
for _ in range(N):
    available += X - int(input())

print(available)
