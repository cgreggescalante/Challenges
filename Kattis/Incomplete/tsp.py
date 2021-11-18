# Travelling Salesperson 2D
import math

n = int(input())

points = [tuple(map(float, input().split())) for _ in range(n)]
distances = [[10**100 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        d = round(math.sqrt(((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)))
        distances[i][j] = d
        distances[j][i] = d

for i in range(n):
    m = min(distances[i])
    for j in range(n):
        distances[i][j] -= m

for j in range(n):
    m = min(distances[i][j] for i in range(n))
    for i in range(n):
        distances[i][j] -= m

for d in distances:
    print(d)

min_distance = sum(distances[a][a+1] for a in range(n - 1))
best_path = []


def rec_path(remain=None, current=None, path=None, dist=0):
    global min_distance, best_path
    if dist > min_distance:
        return
    if remain is None:
        remain = [i for i in range(n)]
    if len(remain) == 0:
        if dist < min_distance:
            min_distance = dist
            best_path = path

    if current is None:
        for c in range(n):
            new_remain = remain.copy()
            new_remain.remove(c)
            rec_path(new_remain, c, [c])
    else:
        pt_dist = sorted([(i, distances[current][i]) for i in remain], key=lambda x: x[1])
        for next_point, d in pt_dist:
            new_remain = remain.copy()
            new_remain.remove(next_point)
            rec_path(new_remain, current, path + [next_point], dist + d)


rec_path()

print(min_distance)
print(best_path)

