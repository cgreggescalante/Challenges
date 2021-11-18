# Transitions and Transversions
from Rosalind.FASTALoader import load

strings = [a for a in load('../Resources/rosalind_tran.txt').values()]

a = strings[0]
b = strings[1]

transitions = 0
transversions = 0

t = {
    'A': 'G',
    'G': 'A',
    'C': 'T',
    'T': 'C'
}

for i in range(len(a)):
    if a[i] != b[i]:
        if t[a[i]] == b[i]:
            transitions += 1
        else:
            transversions += 1

print(transitions / transversions)
