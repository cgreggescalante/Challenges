# Golomb's Self-Describing Sequence

# value, first, last
from tqdm import tqdm

known = [[1, 1, 1]]

n = 2
i = 2
i3 = i ** 3
total = 1

top = 10**6
t = tqdm(range(top))

while True:
    found = False
    start = known[-1][2]
    for r in range(len(known)):
        if known[r][1] <= n <= known[r][2]:
            new_r = [n, start + 1, start + known[r][0]]
            known.append(new_r)
            if n == known[r][2]:
                known.pop(r)
            found = True
            break

    if not found:
        known.append([n, 2, 3])

    if i3 <= known[-1][2]:
        t.update()
        total += known[-1][0]
        i += 1
        i3 = i ** 3
        if i >= top:
            print(i)
            break
    n += 1
print(total)
