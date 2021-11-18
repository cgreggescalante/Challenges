# Find Substrings of a Genome Encoding a Given Amino Acid String
import os

from Rosalind.CodonTable import rna_from_protein
from Rosalind.DNA_to_RNA import rna_to_dna, reverse_complement

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    text = file.readline().strip()
    peptide = file.readline().strip()

rna_target = []
for protein in peptide:
    poss = rna_from_protein(protein)

    if len(rna_target):
        new_targets = []
        for a in rna_target:
            for p in poss:
                new_targets.append(a + p)
        rna_target = new_targets
    else:
        rna_target = poss

dna_target = list(map(rna_to_dna, rna_target))
dna_target.extend(list(map(reverse_complement, dna_target)))

for a in dna_target:
    for _ in range(text.count(a)):
        print(a)

