# Find a Median String
import os

from Rosalind.Misc import number_to_pattern, hamming_distance

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    k = int(lines[0])
    dna = [line.strip() for line in lines[1:]]

k_mers = list(map(lambda i: number_to_pattern(i, k), range(4**k)))
scores = [0 for _ in range(4**k)]

for i in range(len(k_mers)):
    t = 0
    for pattern in dna:
        m = 10**10
        for j in range(len(pattern) - k + 1):
            d = hamming_distance(k_mers[i], pattern[j:j+k])
            if d < m:
                m = d
        t += m
    scores[i] = t

print([k_mers[i] for i in range(len(k_mers)) if scores[i] == min(scores)][0])
