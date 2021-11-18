# Hexagonal Tile Differences
from collections import defaultdict
from math import ceil, sqrt

import primesieve
from tqdm import tqdm

starts = {0: 1}
primes = set(primesieve.primes(10**7))


def ring_start(n):
    if n not in starts:
        starts[n] = 3 * n ** 2 - 3 * n + 2

    return starts[n]


def ring_pos(n):
    r = ceil((-3 + sqrt(12 * n - 3)) / 6)

    start = ring_start(r)

    return r, n - start


def cell_value(ring, pos):
    if ring == 0:
        return 1
    pos %= (ring * 6)

    start = ring_start(ring)

    return start + pos


def get_neighbors(n):
    ring, pos = ring_pos(n)

    """
        Cases:
            Corner: One in, Three out
                pos % ring == 0
            Edge: Two in, Two out
                else
    """

    if pos % ring == 0:
        corner = pos // ring
        outer_pos = (ring + 1) * corner
        return [
            abs(cell_value(ring, pos + 1) - n),
            abs(n - cell_value(ring, pos - 1)),
            n - cell_value(ring - 1, (ring - 1) * corner),
            cell_value(ring + 1, outer_pos - 1) - n,
            cell_value(ring + 1, outer_pos) - n,
            cell_value(ring + 1, outer_pos + 1) - n
        ]
    else:
        inner_pos = int(pos / ring * (ring - 1))
        outer_pos = int(pos * (ring + 1) / ring)
        return [
            abs(cell_value(ring, pos + 1) - n),
            abs(n - cell_value(ring, pos - 1)),
            n - cell_value(ring - 1, inner_pos),
            n - cell_value(ring - 1, inner_pos + 1),
            cell_value(ring + 1, outer_pos) - n,
            cell_value(ring + 1, outer_pos + 1) - n
        ]


pd = [1]
n = 2
end_freq = defaultdict(int)
last_new = 0
target = 2000
t = tqdm(total=target)
while len(pd) < target:
    if n % 100 in {2, 8, 19, 20, 37, 61, 28, 17, 71, 98, 78, 70, 47, 81, 77, 41, 88, 69, 21, 51, 58, 48, 27, 1, 67, 97, 38, 18, 68, 57, 91, 7, 87, 11, 31}:
        neighbors = get_neighbors(n)
        # print(n, neighbors)
        # break
        c = len([a for a in neighbors if a in primes])
        if c == 3:
            # print(n)
            t.update()
            # if not end_freq[n % 100]:
            #     last_new = n
            # end_freq[n % 100] += 1
            pd.append(n)
    n += 1

# for k in sorted(end_freq.keys()):
#     print(k, end_freq[k])

# print(end_freq.keys())
# print(last_new)
# 50 TEST
# assert pd == [1, 2, 8, 19, 20, 37, 61, 128, 217, 271, 398, 919, 1519, 1520, 2978, 3170, 4220, 4447, 4681, 5677, 5941, 6488, 8269, 9920, 10621, 12481, 16651, 17558, 22448, 26227, 29701, 34028, 34669, 35317, 35971, 56719, 60920, 61777, 74419, 75367, 80197, 88238, 93458, 110018, 117019, 125461, 136747, 140618, 156637, 169220]

# 100 TEST
assert pd == [1, 2, 8, 19, 20, 37, 61, 128, 217, 271, 398, 919, 1519, 1520, 2978, 3170, 4220, 4447, 4681, 5677, 5941, 6488, 8269, 9920, 10621, 12481, 16651, 17558, 22448, 26227, 29701, 34028, 34669, 35317, 35971, 56719, 60920, 61777, 74419, 75367, 80197, 88238, 93458, 110018, 117019, 125461, 136747, 140618, 156637, 169220, 172081, 174968, 182288, 183769, 185257, 214670, 216277, 217891, 246248, 265520, 292970, 302419, 331670, 333667, 362269, 370658, 381278, 407377, 416270, 486019, 498169, 540601, 558578, 590077, 600770, 606151, 672607, 704221, 882920, 1000519, 1053170, 1092637, 1121798, 1181269, 1181270, 1203967, 1215398, 1277269, 1277270, 1281187, 1285111, 1332668, 1340677, 1510171, 1566020, 1627298, 1671788, 1698770, 1703287, 1790270]
