# Implement PatterToNumber
import os

from Utils.Misc import pattern_to_number

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    pattern = file.readline().strip()


print(pattern_to_number(pattern))
