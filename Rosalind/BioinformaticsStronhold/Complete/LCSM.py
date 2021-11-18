# Finding a Shared Motif
from Rosalind.FASTALoader import load

data = load('../Resources/rosalind_lcsm.txt')

keys = [k for k in data.keys()]

longest = ""

for i in range(len(data[keys[0]])):
    j = i + 1 + len(longest)
    while j <= len(data[keys[0]]) + 1:
        sub = data[keys[0]][i:j]
        works = True
        for x in range(1, len(keys)):
            if sub not in data[keys[x]]:
                works = False
                break
        if works:
            longest = sub
        else:
            break
        j += 1

print(longest)
