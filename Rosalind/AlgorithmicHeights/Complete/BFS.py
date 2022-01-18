# Breadth-First Search
from collections import defaultdict

neighbors = defaultdict(set)

with open("../Resources/rosalind_bfs.txt", "r") as file:
    v, e = map(int, file.readline().split())
    for line in file.readlines():
        a, b = map(int, line.split())
        neighbors[a].add(b)

distances = [-1 for _ in range(v)]
not_visited = set(range(v))

distances[0] = 0

added = True
while added:
    added = False
    new_distances = distances.copy()
    for i, d in enumerate(distances):
        if d > -1:
            for n in neighbors[i + 1]:
                if distances[n - 1] < 0:
                    new_distances[n - 1] = d + 1
                    added = True
    distances = new_distances

print(' '.join(map(str, distances)))
