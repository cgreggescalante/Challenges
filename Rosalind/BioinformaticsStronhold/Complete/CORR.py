# Error Correction in Reads
from Utils.DNA_to_RNA import reverse_complement
from Utils.FASTALoader import load

data = [a for a in load('../Resources/rosalind_corr.txt').values()]

good = [False for _ in range(len(data))]
for i in range(len(data)):
    rev = reverse_complement(data[i])
    for j in range(len(data)):
        if i != j:
            if data[j] == data[i] or rev == data[j]:
                good[i] = True

correct = [data[a] for a in range(len(data)) if good[a]]
incorrect = [data[a] for a in range(len(data)) if not good[a]]
nc = {}
for a in correct:
    nc[a] = 0
correct = [a for a in nc.keys()]

for a in incorrect:
    for b in correct:
        c = len([i for i in range(len(a)) if a[i] != b[i]])
        if c == 1:
            print(a + "->" + b)
            break
        rev = reverse_complement(b)
        c = len([i for i in range(len(a)) if a[i] != rev[i]])
        if c == 1:
            print(a + "->" + rev)
            break
