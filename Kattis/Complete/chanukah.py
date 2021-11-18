# Chanukah Challenge

P = int(input())

for _ in range(P):
    k, n = map(int, input().split())
    print(k, (n + 1) * n // 2 + n)
