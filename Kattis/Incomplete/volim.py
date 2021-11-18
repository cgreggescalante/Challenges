# Volim

K = int(input())
N = int(input())

T = 210

for _ in range(N):
    t, z = input().split()
    t = int(t)

    if t >= T:
        break
    if z == "T":
        K += 1
        K %= 8
    T -= t

print(K)
