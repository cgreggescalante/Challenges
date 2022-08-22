# Criss Cross
from collections import defaultdict
from itertools import permutations

from tqdm import tqdm


def sum_to_n(n, count=4, prev=0):
    if count == 0:
        if n == 0:
            return [tuple()]
        return []

    options = []
    for a in range(prev, min(n, 9) + 1):
        for o in sum_to_n(n - a, count - 1, a):
            options.append((a,) + o)
    return options


c = 0

for s in range(37):
    options = set()
    bd = [defaultdict(set) for _ in range(4)]

    for seed in sum_to_n(s):
        for p in permutations(seed):
            options.add(p)
            for i in range(4):
                bd[i][p[i]].add(p)

    for a0 in tqdm(options):
        d0s = bd[0][a0[0]]
        for d0 in d0s:
            a3s = bd[0][d0[3]]
            for a3 in a3s:
                d3s = bd[0][a0[3]].intersection(bd[3][a3[3]])
                for d3 in d3s:
                    a1s = bd[0][d0[1]].intersection(bd[3][d3[1]])
                    for a1 in a1s:
                        d1s = bd[0][a0[1]].intersection(bd[1][a1[1]]).intersection(bd[3][a3[1]])
                        for d1 in d1s:
                            d2s = bd[0][a0[2]].intersection(bd[1][a1[2]]).intersection(bd[3][a3[2]])
                            for d2 in d2s:
                                a2 = (d0[2], d1[2], d2[2], d3[2])
                                if a2 not in options:
                                    continue

                                nd = (a0[0], a1[1], a2[2], a3[3])
                                if nd not in options:
                                    continue

                                pd = (a0[3], a1[2], a2[1], a3[0])
                                if pd in options:
                                    c += 1

print(c)
