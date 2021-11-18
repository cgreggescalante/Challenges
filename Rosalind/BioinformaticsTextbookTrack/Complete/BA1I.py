# Find the Most Frequent Words with Mismatches in a String
import os

from tqdm import tqdm

from Rosalind.Misc import hamming_distance, d_neighborhood

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    text = lines[0].strip()
    k, d = map(int, lines[1].split())

present = {text[i:i+k]: 0 for i in range(len(text) - k + 1)}

k_mers = {}
for base in present:
    for neighbor in d_neighborhood(base, d):
        k_mers[neighbor] = 0

for i in tqdm(range(len(text) - k + 1)):
    for mers in k_mers:
        if hamming_distance(text[i:i+k], mers) <= d:
            k_mers[mers] += 1

print(' '.join({k for k in k_mers if k_mers[k] == max(k_mers.values())}))
