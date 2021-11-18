# Reconstruct a String from its k-mer Composition
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    lines = file.readlines()
    k = int(lines[0])
    k_mers = [line.strip() for line in lines[1:]]

while len(k_mers) > 1:
    i = 0
    while i < len(k_mers) - 1:
        j = i + 1
        while j < len(k_mers):
            # print(k_mers[i][-k + 1:], k_mers[j][:k - 1])
            if k_mers[i][-k + 1:] == k_mers[j][:k - 1]:
                k_mers[i] += k_mers[j][k - 1:]
                k_mers.pop(j)
            elif k_mers[j][-k + 1:] == k_mers[i][:k - 1]:
                k_mers[j] += k_mers[i][k - 1:]
                k_mers.pop(i)
            else:
                j += 1
        i += 1

print(k_mers[0])
