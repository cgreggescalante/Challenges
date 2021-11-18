# Nasty Hacks

n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())
    d = e - r
    if d == c:
        print("does not matter")
    elif d > c:
        print("advertise")
    else:
        print("do not advertise")
