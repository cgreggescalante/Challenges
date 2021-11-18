# Rating Problems

n, k = map(int, input().split())

r = sum([int(input()) for _ in range(k)])

print((r + (n - k) * -3) / n, (r + (n - k) * 3) / n)
