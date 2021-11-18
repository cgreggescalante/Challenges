# Transit Woes

s, t, n = map(int, input().split())

d = list(map(int, input().split()))

b = list(map(int, input().split()))

c = list(map(int, input().split()))

current = s

for i in range(n):
    current += d[i]
    if current % c[i]:
        current += c[i] - (current % c[i])
    current += b[i]

current += d[-1]

print("yes" if current <= t else "no")
