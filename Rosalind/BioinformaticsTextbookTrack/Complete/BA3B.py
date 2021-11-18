# Reconstruct a String from its Genome Path
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    path = [line.strip() for line in file.readlines()]

print(''.join([p[0] for p in path[:-1]]), path[-1], sep="")
