# Double-Degree Array
from collections import defaultdict

neighbors = defaultdict(set)
degrees = defaultdict(int)

with open("../Resources/rosalind_ddeg.txt", "r") as file:
    n, m = map(int, file.readline().split())
    for line in file.readlines():
        a, b = map(int, line.split())
        neighbors[a].add(b)
        neighbors[b].add(a)
        degrees[a] += 1
        degrees[b] += 1

for i in range(1, n + 1):
    print(sum(map(lambda x: degrees[x], neighbors[i])), end=" ")
