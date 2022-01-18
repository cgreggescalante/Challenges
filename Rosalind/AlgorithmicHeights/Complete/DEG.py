# Degree Array
from collections import defaultdict

d = defaultdict(int)

with open("../Resources/rosalind_deg.txt") as file:
    lines = file.readlines()[1:]
    for line in lines:
        a, b = map(int, line.split())
        d[a] += 1
        d[b] += 1

print(' '.join(map(lambda x: str(x[1]), sorted(d.items()))))
