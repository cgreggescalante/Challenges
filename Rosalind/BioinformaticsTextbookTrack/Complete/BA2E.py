# Implement GreedyMotifSearch with Pseudocounts
import os

from Utils.Misc import greedy_motif_search

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    k, t = map(int, lines[0].split())
    dna = [line.strip() for line in lines[1:]]

print('\n'.join(greedy_motif_search(dna, k, t, pseudocounts=True)))
