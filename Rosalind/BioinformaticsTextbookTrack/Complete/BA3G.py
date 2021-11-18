# Find an Eulerian Path in a Graph
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    edges = {}
    for line in file.readlines():
        spl = line.strip().split(" -> ")
        node = int(spl[0])
        results = list(map(int, spl[1].split(",")))
        edges[node] = results

start = -1
for a in edges:
    i = 0
    for b in edges:
        i += edges[b].count(a)
    if i + 1 == len(edges[a]):
        start = a

path = [start]

cycle = []

while path:
    current = path[-1]

    if current in edges and len(edges[current]):
        next_vertex = edges[current].pop()

        path.append(next_vertex)
    else:
        cycle.append(path.pop())

print("->".join(map(str, cycle[::-1])))
