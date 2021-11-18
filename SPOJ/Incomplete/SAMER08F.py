# Feynman

n = int(input())

while n:
    t = 0
    for i in range(1, n + 1):
        t += (n - i + 1) ** 2
    print(t)
    n = int(input())
