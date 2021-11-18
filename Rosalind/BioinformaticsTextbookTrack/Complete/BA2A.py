# Implement MotifEnumeration
import os.path

from Rosalind.Misc import motif_enumeration

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    k, d = map(int, lines[0].split())
    patterns = [line.strip() for line in lines[1:]]


print(' '.join(motif_enumeration(patterns, k, d)))
