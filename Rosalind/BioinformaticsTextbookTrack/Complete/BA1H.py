# Find All Approximate Occurrences of a Pattern in a String
import os

from Rosalind.Misc import hamming_distance

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    pattern = lines[0].strip()
    text = lines[1].strip()
    d = int(lines[2])


for i in range(len(text) - len(pattern) + 1):
    if hamming_distance(text[i:i+len(pattern)], pattern) <= d:
        print(i, end=" ")
