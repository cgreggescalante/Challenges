# Connected Components
from collections import defaultdict

edges = defaultdict(set)

with open("../Resources/rosalind_cc.txt", "r") as file:
    v, e = map(int, file.readline().split())
    for _ in range(e):
        a, b = map(int, file.readline().split())
        edges[a].add(b)
        edges[b].add(a)

components = 0
visited = set()

for i in range(1, v + 1):
    if i in visited:
        continue
    visited.add(i)
    layer = {i}
    local_visited = {i}
    while layer:
        new_layer = set()
        for vertex in layer:
            for edge in edges[vertex]:
                if edge not in local_visited:
                    local_visited.add(edge)
                    visited.add(edge)
                    new_layer.add(edge)
        layer = new_layer
    components += 1

print(components)

