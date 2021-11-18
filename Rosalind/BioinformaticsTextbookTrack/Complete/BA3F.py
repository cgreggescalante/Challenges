# Find a Eulerian Cycle in a Graph
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    edges = {}
    for line in file.readlines():
        spl = line.strip().split(" -> ")
        node = int(spl[0])
        results = list(map(int, spl[1].split(",")))
        edges[node] = results


path = [0]

cycle = []

while path:
    current = path[-1]

    if len(edges[current]):
        next_vertex = edges[current].pop()

        path.append(next_vertex)
    else:
        cycle.append(path.pop())

print("->".join(map(str, cycle[::-1])))
