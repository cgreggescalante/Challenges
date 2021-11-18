# Almost Equilateral Triangles
from math import sqrt

from tqdm import tqdm

top = 1000000000
total = 0
a = 1

for a in tqdm(range(1, 333333336)):
    if a > 1:
        s = (3 * a - 1) / 2
        area = sqrt(s * (s - a) ** 2 * (s - a + 1))
        if int(area) == area:
            total += a * 3 - 1
    if a * 3 + 1 > top:
        break
    s = (3 * a + 1) / 2
    area = sqrt(s * (s - a) ** 2 * (s - a - 1))
    if int(area) == area:
        total += a * 3 + 1

print(total)