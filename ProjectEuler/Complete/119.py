# Digit Power Sum
from tqdm import tqdm

x = 0
works = []

while len(works) < 30:
    print(len(works), x)
    print(sorted(works))
    possibles = {}
    for p in range(2, 100):
        possibles[p] = {}

    end = 2**(x + 1)
    if x == 0:
        start = 2
    else:
        start = 7**x

    t2 = end ** .5

    for i in tqdm(range(2, int(t2))):
        p = 2
        while i**p < end:
            possibles[p][i**p] = 0
            p += 1
        i += 1

    for p in tqdm(sorted(possibles.keys())):
        for i in sorted(possibles[p].keys()):
            t = sum([int(c) for c in str(i)])
            if t**p == i and i not in works:
                works.append(i)

    x += 1
    print()

for i in range(len(works)):
    print(i + 1, works[i])