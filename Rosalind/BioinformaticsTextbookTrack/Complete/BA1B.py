# Find the Most Frequent Words in a String
import os
from collections import defaultdict

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    text = lines[0].strip()
    k = int(lines[1])


k_mers = defaultdict(int)

for i in range(len(text) - k):
    k_mers[text[i:i+k]] += 1

k_mers = {k: k_mers[k] for k in sorted(k_mers.keys())}
for k, v in k_mers.items():
    if v == max(k_mers.values()):
        print(k, end=" ")
