# Implement NumberToPattern
import os

from Utils.Misc import number_to_pattern

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    index = int(lines[0])
    k = int(lines[1])


print(number_to_pattern(index, k))
