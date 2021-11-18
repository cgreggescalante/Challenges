# Construct the Overlap Graph of a Collection of k-mers
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    patterns = [line.strip() for line in file.readlines()]

for a in patterns:
    for b in patterns:
        if b.startswith(a[1:]):
            print(a, b, sep=" -> ")
