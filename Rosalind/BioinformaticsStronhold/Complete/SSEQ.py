# Finding a Spliced Motif
from Utils.FASTALoader import load

data = load('../Resources/rosalind_sseq.txt')
values = [a for a in data.values()]
s = values[0]
t = values[1]

i = 0
indices = []
while len(t) > 0:
    if s[i] == t[0]:
        indices.append(str(i + 1))
        t = t[1:]
    i += 1

print(' '.join(indices))
