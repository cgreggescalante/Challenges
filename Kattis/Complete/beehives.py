# Beehives

fight, n = map(float, input().split())
fight **= 2

while fight + n > 0:
    pts = [list(map(float, input().split())) for _ in range(int(n))]
    sour = 0
    for i in range(int(n)):
        for j in range(int(n)):
            if i == j:
                continue
            d = (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2
            if d < fight:
                sour += 1
                break
    print(f"{sour} sour, {int(n - sour)} sweet")
    fight, n = map(float, input().split())
    fight **= 2
