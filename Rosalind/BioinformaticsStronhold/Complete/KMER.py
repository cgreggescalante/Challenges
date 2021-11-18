# K-Mer Composition
from Utils.FASTALoader import load

s = [a for a in load('../Resources/rosalind_kmer.txt').values()][0]

letters = ['A', 'C', 'G', 'T']

options = letters[:]

for i in range(3):
    new_options = []
    for a in options:
        for b in letters:
            new_options.append(a + b)
    options = new_options

counters = {}
for a in options:
    counters[a] = 0

for i in range(len(s) - 3):
    counters[s[i:i+4]] += 1

print(' '.join([str(counters[a]) for a in options]))
