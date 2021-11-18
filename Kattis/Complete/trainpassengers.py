# Train Passengers

C, n = map(int, input().split())

curr = 0
poss = True

for _ in range(n):
    a, b, c, = map(int, input().split())
    curr -= a
    if curr < 0:
        poss = False
        break
    curr += b
    if curr > C:
        poss = False
        break
    if c > 0 and curr < C:
        poss = False
        break

if curr > 0:
    poss = False

print("possible" if poss else "impossible")
