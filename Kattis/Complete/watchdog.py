# Watchdog

N = int(input())


def check(h, s):
    for x in range(s+1):
        for y in range(s+1):
            max_d = min(x, y, s - x, s - y)
            works = True
            for hatch in h:
                d = ((x-hatch[0])**2 + (y-hatch[1])**2)**.5
                if d > max_d or x == hatch[0] and y == hatch[1]:
                    works = False
                    break
            if works:
                return str(x) + ' ' + str(y)
    return "poodle"


for _ in range(N):
    S, H = map(int, input().split())
    hatches = []
    for _ in range(H):
        x, y = map(int, input().split())
        hatches.append([x, y])
    works = False
    print(check(hatches, S))
