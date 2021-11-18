# Speed Limit

n = int(input())

while n > 0:
    d = 0
    prev = 0
    for _ in range(n):
        s, t = map(int, input().split())
        d += s * (t - prev)
        prev = t
    print(d, "miles")
    n = int(input())
