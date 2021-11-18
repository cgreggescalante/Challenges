# Find a Profile-most Probable k-mer in a String
import os

from Rosalind.Misc import pattern_to_number

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    text = lines[0].strip()
    k = int(lines[1])
    profile = [list(map(float, line.split())) for line in lines[2:6]]

k_mers = {text[i:i+k]: 0 for i in range(len(text) - k + 1)}

for mer in k_mers:
    t = 1
    for i in range(len(mer)):
        t *= profile[pattern_to_number(mer[i])][i]
    k_mers[mer] = t

print([k for k in k_mers if k_mers[k] == max(k_mers.values())][0])
