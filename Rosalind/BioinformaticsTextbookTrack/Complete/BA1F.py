# Find a Position in a Genome Minimizing the Skew
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    genome = file.readline().strip()

c = 0
smallest = 0
min_i = [0]

for i in range(len(genome)):
    if genome[i] == "G":
        c += 1
    elif genome[i] == "C":
        c -= 1
    if c < smallest:
        smallest = c
        min_i = [i + 1]
    elif c == smallest:
        min_i.append(i + 1)

print(' '.join(map(str, min_i)))
