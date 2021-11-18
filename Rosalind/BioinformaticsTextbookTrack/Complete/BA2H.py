# Implement DistanceBetweenPatternAndStrings
import os

from Rosalind.Misc import distance_between_pattern_and_strings

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    pattern = lines[0].strip()
    dna = lines[1].split()


print(distance_between_pattern_and_strings(pattern, dna))
