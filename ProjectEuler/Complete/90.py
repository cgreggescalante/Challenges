# Cube Digit Pairs
from itertools import combinations

cubes = {1, 4, 9, 16, 25, 36, 49, 64, 81}


def forms_all(a, b):
    poss = set()
    if 6 in a:
        a.add(9)
    if 9 in a:
        a.add(6)
    if 6 in b:
        b.add(9)
    if 9 in b:
        b.add(6)
    for x in a:
        for y in b:
            poss.add(int(f"{x}{y}"))
            poss.add(int(f"{y}{x}"))
    return cubes.issubset(poss)


used = set()
c = 0

for i in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6):
    a = set(i)
    for j in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6):
        b = set(j)
        if not (f"{a}{b}" in used or f"{b}{a}" in used):
            used.add(f"{a}{b}")
            if forms_all(a.copy(), b):
                c += 1

print(c)
