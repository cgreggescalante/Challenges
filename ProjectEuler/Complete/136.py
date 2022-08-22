# Singleton difference
from collections import defaultdict

from tqdm import tqdm

target = 50000000

counts = defaultdict(int)

for gap in tqdm(range(target)):
    over_start = 0
    over_end = 0
    if 4 * gap ** 2 > target:
        s = int((4 * gap ** 2 - target) ** .5)
        over_start = gap - s
        over_end = gap + s
    z = 1
    while z < 3 * gap + 1:
        n = -z**2 + 3 * gap ** 2 + 2 * z * gap
        if 0 < n < target:
            counts[n] += 1
        z += 1
        if over_start <= z <= over_end:
            z = over_end + 1

print(sum(1 for a in counts if counts[a] == 1))
