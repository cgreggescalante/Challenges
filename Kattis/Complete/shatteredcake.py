# Shattered Cake

W = int(input())
N = int(input())

a = 0

for _ in range(N):
    w, l = map(int, input().split())
    a += w * l

print(a // W)
