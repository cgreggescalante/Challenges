# Jabuke

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

y23 = y2 - y3
x32 = x3 - x2
y31 = y3 - y1
x13 = x1 - x3
det = y23 * x13 - x32 * y31
minD = min(det, 0)
maxD = max(det, 0)

total = 0

for x, y in points:
    dx = x - x3
    dy = y - y3
    a = y23 * dx + x13 * dy
    if a < minD or a > maxD:
        continue
    b = y31 * dx + x13 * dy
    if b < minD or b > maxD:
        continue
    c = det - a - b
    if c < minD or c > maxD:
        continue
    total += 1

print(total)
