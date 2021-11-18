# Find All Occurrences of a Pattern in a String
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    pattern = lines[0].strip()
    genome = lines[1].strip()


print(' '.join(map(str, [i for i in range(len(genome)) if genome[i:].startswith(pattern)])))
