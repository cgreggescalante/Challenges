# Speeding Up Motif Finding
from Rosalind.FASTALoader import load

s = [a for a in load('../Resources/rosalind_kmp.txt').values()][0]

p = [0 for _ in range(len(s))]

options = [a for a in range(1, len(s)) if s[a] == s[0]]
for a in options:
    p[a] = 1

i = 1
while len(options) > 0:
    j = 0
    while j < len(options):
        if s[options[j] + i] != s[i]:
            options = options[:j] + options[j+1:]
        else:
            p[options[j] + i] = i + 1
            j += 1
    i += 1

print(' '.join([str(a) for a in p]))

