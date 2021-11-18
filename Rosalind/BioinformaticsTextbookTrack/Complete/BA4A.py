# Translate an RNA String into an Amino Acid String
import os

from Rosalind.CodonTable import protein_from_rna

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    pattern = file.readline().strip()


while len(pattern):
    protein = protein_from_rna(pattern[:3])
    if protein == "Stop":
        break
    print(protein, end="")
    pattern = pattern[3:]
