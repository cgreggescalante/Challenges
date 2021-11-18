# Find the Reverse Complement of a String
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    pattern = file.readline().strip()

complements = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

print(''.join(map(lambda x: complements[x], pattern[::-1])))
