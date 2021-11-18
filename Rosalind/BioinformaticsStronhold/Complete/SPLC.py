# RNA Splicing
from Utils.CodonTable import protein_from_rna
from Utils.DNA_to_RNA import dna_to_rna

s = None
introns = []

with open("../Resources/rosalind_splc.txt", 'r') as file:
    lines = file.readlines()[1:]
    s = ""
    while not lines[0].startswith('>'):
        s += lines[0][:-1]
        lines = lines[1:]

    while len(lines) > 0:
        lines = lines[1:]
        a = ""
        while len(lines) > 0 and not lines[0].startswith('>'):
            a += lines[0]
            if a.endswith('\n'):
                a = a[:-1]
            lines = lines[1:]
        introns.append(a)

found = True
while found:
    found = False
    pos = 0
    l = 0
    for i in range(len(s)):
        for j in introns:
            if s[i:i+len(j)] == j:
                found = True
                pos = i
                l = len(j)
                break
        if found:
            break

    if found:
        s = s[:pos] + s[pos+l:]

rna = dna_to_rna(s)

sequence = ""
while len(rna) > 2:
    p = protein_from_rna(rna[:3])
    if p == 'Stop':
        break
    sequence += p
    rna = rna[3:]

print(sequence)
