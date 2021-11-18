# Generate the Frequency Array of a String
import os

from Utils.Misc import pattern_to_number

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    text = lines[0].strip()
    k = int(lines[1])


counts = [0 for _ in range(4**k)]

for i in range(len(text) - k + 1):
    counts[pattern_to_number(text[i: i + k])] += 1

print(' '.join(map(str, counts)))
