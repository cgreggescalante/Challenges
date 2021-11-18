# Implement GibbsSampler
import os

from Rosalind.Misc import gibbs_sampler

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    k, t, N = map(int, file.readline().split())
    dna = [line.strip() for line in file.readlines()]


motifs = []
for a in range(20):
    motifs.append(gibbs_sampler(dna, k, t, N))

print(motifs)
