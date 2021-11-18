# Same Differences
from tqdm import tqdm

n = {}

for c in tqdm(range(1, 250001)):
    x = 1
    while x < 3 * c:
        val = 3 * c ** 2 + 2 * x * c - x ** 2
        if val >= 1000000:
            break
        if 0 < val:
            try:
                n[val] += 1
            except KeyError:
                n[val] = 1
        x += 1

    if c >= 500:
        x = 3 * c
        while True:
            val = 3 * c ** 2 + 2 * x * c - x ** 2
            if val >= 1000000:
                break
            if val > 0:
                try:
                    n[val] += 1
                except KeyError:
                    n[val] = 1
            x -= 1
    c += 1

print(len([a for a in n.values() if a == 10]))
