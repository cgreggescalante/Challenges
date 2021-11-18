# Compute the Hamming Distance Between Two Strings
import os

from Utils.Misc import hamming_distance

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    a = lines[0].strip()
    b = lines[1].strip()


print(hamming_distance(a, b))
