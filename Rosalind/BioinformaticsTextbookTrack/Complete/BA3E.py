# Construct the De Bruijn Graph of a Collection of k-mers
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    patterns = [line.strip() for line in file.readlines()]

graph = {pattern[:-1]: [] for pattern in patterns}

for pattern in patterns:
    graph[pattern[:-1]].append(pattern[1:])

for k, v in graph.items():
    print(k, ','.join(v), sep=" -> ")
