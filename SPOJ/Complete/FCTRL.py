# Factorial

T = int(input())

for _ in range(T):
    n = int(input())

    x = 5
    t = 0
    while x <= n:
        t += n // x
        x *= 5
    print(t)
