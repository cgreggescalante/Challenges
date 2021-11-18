# Army Strength (Hard)

T = int(input())

for _ in range(T):
    input()
    ng, nm = map(int, input().split())

    g = sorted(list(map(int, input().split())))
    m = sorted(list(map(int, input().split())))
    gi = 0
    mi = 0
    while gi < ng and mi < nm:
        if g[gi] < m[mi]:
            gi += 1
        else:
            mi += 1

    print("Godzilla" if mi == nm else "MechaGodzilla")
