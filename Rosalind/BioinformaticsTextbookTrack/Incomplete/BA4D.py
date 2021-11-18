# Compute the Number of Peptides of Given Total Mass
import math
import os

with open(f"../Resources/rosalind_{os.path.basename(__file__)[:-3].lower()}.txt") as file:
    m = int(file.readline())

table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891,
         'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858,
         'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}

values = sorted(list(table.values()))
names = {v: k for k, v in table.items()}


def count_combs(left, i, comb, add):
    if add:
        comb.append(add)
    if int(left) == 0 or (i + 1) == len(values):
        if (i + 1) == len(values) and int(left) > 0:
            if left % values[i]:
                return 0
            comb.append((left / values[i], values[i]))
            i += 1
        while i < len(values):
            comb.append((0, values[i]))
            i += 1
        s = ''.join(n * names[c] for n, c in comb)

        freq = [n for n, c in comb if n > 0]
        f = 1
        for v in freq:
            f *= math.factorial(v)

        return math.factorial(len(s)) // f
    cur = values[i]
    return sum(count_combs(left - x * cur, i + 1, comb[:], (x, cur)) for x in range(0, int(left / cur) + 1))


print(count_combs(m, 0, [], None))
