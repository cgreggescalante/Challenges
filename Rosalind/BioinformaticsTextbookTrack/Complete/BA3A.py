# Generate the k-mer Composition of a String
import os

from Utils.Misc import k_mer_composition

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    k = int(file.readline())
    text = file.readline().strip()

print("\n".join(k_mer_composition(text, k)))
