# Find Patterns Forming Clumps in a String
import os
from collections import defaultdict

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    genome = lines[0].strip()
    k, L, t = map(int, lines[1].split())

k_mers = defaultdict(int)

for i in range(len(genome) - k + 1):
    k_mers[genome[i:i+k]] += 1

k_mers = {m for m in k_mers if k_mers[m] >= t}

valid = set()
for i in range(len(genome) - L + 1):
    counts = defaultdict(int)
    for j in range(i, i + L - k + 1):
        if genome[j:j+k] in k_mers:
            counts[genome[j:j+k]] += 1
    counts = {m for m in counts if counts[m] >= t}
    valid.update(counts)

print(' '.join(valid))
