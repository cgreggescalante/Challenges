# Find Frequent Words with Mismatches and Reverse Complements
import os

from tqdm import tqdm

from Rosalind.DNA_to_RNA import reverse_complement
from Rosalind.Misc import hamming_distance, d_neighborhood

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    text = lines[0].strip()
    k, d = map(int, lines[1].split())

k_mers = {}
for base in {text[i:i+k]: 0 for i in range(len(text) - k + 1)}:
    for neighbor in d_neighborhood(base, d):
        k_mers[neighbor] = 0
    for neighbor in d_neighborhood(reverse_complement(base), d):
        k_mers[neighbor] = 0


for i in tqdm(range(len(text) - k + 1)):
    for mers in k_mers:
        if hamming_distance(text[i:i+k], mers) <= d:
            k_mers[mers] += 1
        if hamming_distance(text[i:i+k], reverse_complement(mers)) <= d:
            k_mers[mers] += 1

k_mers = {k: v for k, v in k_mers.items() if v == max(k_mers.values())}

print(' '.join(sorted({k for k in k_mers if k_mers[k] == max(k_mers.values())})))
