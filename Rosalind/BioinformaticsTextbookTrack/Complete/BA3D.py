# Construct the De Bruijn Graph of a String
import os

from Utils.Misc import k_mer_composition

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    k = int(file.readline())
    text = file.readline().strip()

k_mers = k_mer_composition(text, k)

graph = {k_mer[:-1]: [] for k_mer in k_mers}

for k_mer in k_mers:
    graph[k_mer[:-1]].append(k_mer[1:])

for k, v in graph.items():
    print(k, ','.join(v), sep=" -> ")
