# Finding a Protein Motif
from Utils.FASTALoader import load

proteins = []

with open('../Resources/rosalind_mprt.txt', 'r') as file:
    proteins = [a for a in file.readlines()]

    for i in range(len(proteins)):
        if proteins[i][-1] == '\n':
            proteins[i] = proteins[i][:-1]


for p in proteins:
    positions = []
    sequence = load('http://www.uniprot.org/uniprot/' + p + '.fasta')

    for i in range(len(sequence) - 3):
        if sequence[i] == 'N' and sequence[i + 1] != 'P' and sequence[i + 2] in ['S', 'T'] and sequence[i + 3] != 'P':
            positions.append(str(i + 1))

    if len(positions) > 0:
        print(p)
        print(' '.join(positions))
