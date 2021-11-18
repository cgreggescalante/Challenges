# Black Friday

n = int(input())

rolls = list(map(int, input().split()))

d = {}

u = 0

for r in rolls:
    if r in d:
        d[r] += 1
    else:
        d[r] = 1

for r in d:
    if d[r] == 1 and r > u:
        u = r

print(rolls.index(u) + 1 if u else "none")
