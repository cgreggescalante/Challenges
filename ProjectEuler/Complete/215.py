# Crack-free Walls


def unique_permutations(seq):
    """
    Yield only unique permutations of seq in an efficient way.

    A python implementation of Knuth's "Algorithm L", also known from the
    std::next_permutation function of C++, and as the permutation algorithm
    of Narayana Pandita.
    """
    i_indices = list(range(len(seq) - 1, -1, -1))
    k_indices = i_indices[1:]

    while True:
        yield seq

        for k in k_indices:
            if seq[k] < seq[k + 1]:
                break
        else:
            return

        k_val = seq[k]

        for i in i_indices:
            if k_val < seq[i]:
                break

        (seq[k], seq[i]) = (seq[i], seq[k])

        seq[k + 1:] = seq[-1:k:-1]


combinations = [
    [16, 0],
    [13, 2],
    [10, 4],
    [7, 6],
    [4, 8],
    [1, 10]
]

rows = []

for c in combinations:
    arr = [2 for _ in range(c[0])] + [3 for _ in range(c[1])]

    for o in unique_permutations(arr):
        rows.append({sum(o[:i]) for i in range(1, len(o))})


pair_dict = {}
c_dict = {}

for i in range(len(rows)):
    pair_dict[i] = set()
    c_dict[i] = 0
    for j in range(len(rows)):
        if i == j:
            continue
        if rows[i].isdisjoint(rows[j]):
            pair_dict[i].add(j)
            c_dict[i] += 1


total = 0
known = {}


def rec_e(i, depth=0):
    if i in known and depth in known[i]:
        return known[i][depth]
    if depth == 8:
        return c_dict[i]

    t = 0
    for j in pair_dict[i]:
        t += rec_e(j, depth + 1)

    if i not in known:
        known[i] = {}

    known[i][depth] = t

    return t


for i in pair_dict:
    total += rec_e(i)

assert total == 806844323190414
