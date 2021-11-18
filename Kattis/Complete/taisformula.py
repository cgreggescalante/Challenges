# Tai's Formula

n = int(input())

prev_t, prev_v = map(float, input().split())
a = 0

for _ in range(n-1):
    t, v = map(float, input().split())
    a += (v + prev_v) / 2 * (t - prev_t)
    prev_t, prev_v = t, v

print(a / 1000)
