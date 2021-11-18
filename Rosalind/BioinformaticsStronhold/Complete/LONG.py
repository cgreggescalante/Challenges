# Genome Assembly as Shortest Superstring
from Rosalind.FASTALoader import load

strings = [a for a in load('../Resources/rosalind_long.txt').values()]

while len(strings) > 1:
    max_o = 0
    max_i = 0
    front = False
    for j in range(1, len(strings)):
        i = 1
        while i < len(strings[j]):
            if strings[0][-i:] == strings[j][:i]:
                if i > max_o:
                    front = False
                    max_o = i
                    max_i = j
            i += 1
    for j in range(1, len(strings)):
        i = 2
        while i < len(strings[j]):
            if strings[0][:i] == strings[j][-i:]:
                if i > max_o:
                    front = True
                    max_o = i
                    max_i = j
            i += 1
    print(max_o, front)
    if front:
        strings[0] = strings[max_i][:-max_o] + strings[0]
    else:
        strings[0] = strings[0] + strings[max_i][max_o:]
    strings = strings[:max_i] + strings[max_i+1:]

    i = 1
    while i < len(strings):
        if strings[i] in strings[0]:
            strings = strings[:i] + strings[i+1:]
        else:
            i += 1

print(strings[0])
