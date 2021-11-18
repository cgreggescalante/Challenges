# Compute the Probability of a Hidden Path
import os

path = None
transition_matrix = None

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    path = lines[0].strip()
    transition_matrix = {
        "A": {"A": float(lines[-2].split()[1]), "B": float(lines[-2].split()[2])},
        "B": {"A": float(lines[-1].split()[1]), "B": float(lines[-1].split()[2])}
    }

t = .5
for i in range(1, len(path)):
    t *= transition_matrix[path[i]][path[i-1]]

print(f"{t:1.11e}")
