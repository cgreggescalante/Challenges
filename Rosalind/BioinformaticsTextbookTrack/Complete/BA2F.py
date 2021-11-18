# Implement RandomizedMotifSearch
import os

from Utils.Misc import randomized_motif_search

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    k, t = map(int, lines[0].split())
    dna = [line.strip() for line in lines[1:]]


motifs = [randomized_motif_search(dna, k, t) for _ in range(1000)]

best = [motifs[i] for i in range(len(motifs)) if motifs[i][1] == min(map(lambda x: x[1], motifs))][0]

print('\n'.join(best[0]))
print(best[1])
