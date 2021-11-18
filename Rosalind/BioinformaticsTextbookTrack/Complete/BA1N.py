# Generate the d-Neighborhood of a String
import os

from Rosalind.Misc import d_neighborhood

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    pattern = lines[0].strip()
    d = int(lines[1])

print('\n'.join(sorted(d_neighborhood(pattern, d))))
