# Mixed Fractions

n, d = map(int, input().split())

while n + d > 0:
    print(f"{n // d} {n % d} / {d}")
    n, d = map(int, input().split())
