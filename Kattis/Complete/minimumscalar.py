# Minimum Scalar Product

T = int(input())

for x in range(T):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))[::-1]
    p = sum([i * j for i, j in zip(a, b)])
    print(f"Case #{x+1}: {p}")
