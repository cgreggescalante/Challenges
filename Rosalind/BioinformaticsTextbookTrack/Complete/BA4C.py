# Generate the Theoretical Spectrum of a Cyclic Peptide
import os

from Utils.MonoisotopicMassTable import mass

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    peptide = file.readline().strip()

spectrum = [0]

for i in range(1, len(peptide)):
    for j in range(len(peptide)):
        if i + j <= len(peptide):
            a = peptide[j:(i + j)]
        else:
            a = peptide[j:] + peptide[:(i + j) % len(peptide)]
        spectrum.append(int(mass(a)))

spectrum.append(int(mass(peptide)))

print(' '.join(map(str, spectrum)))
