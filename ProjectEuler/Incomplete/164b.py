# Numbers for which no three consecutive digits have a sum greater than a given value
from tqdm import tqdm

max_d = 18
next_two = {}
next_three = {}
next_four = {}
next_five = {}
next_six = {}
starts = set()
for a in range(10):
    for b in range(10 - a):
        v = f"{a}{b}"
        next_two[v] = set()
        next_three[v] = set()
        next_four[v] = set()
        next_five[v] = set()
        next_six[v] = set()
        for c in range(10 - a - b):
            for d in range(10 - b - c):
                next_two[v].add(f"{c}{d}")
                for e in range(10 - c - d):
                    next_three[v].add(f"{c}{d}{e}")
                    for f in range(10 - d - e):
                        next_four[v].add(f"{c}{d}{e}{f}")
                        for g in range(10 - e - f):
                            next_five[v].add(f"{c}{d}{e}{f}{g}")
                            for h in range(10 - f - g):
                                next_six[v].add(f"{c}{d}{e}{f}{g}{h}")
                                for i in range(10 - g - h):
                                    if c:
                                        starts.add(f"{c}{d}{e}{f}{g}{h}{i}")


for k in next_two:
    next_two[k] = len(next_two[k])
    next_three[k] = len(next_three[k])
    next_four[k] = len(next_four[k])
    next_five[k] = len(next_five[k])


def recursive(arr=None):
    s = 0
    # If initial call, seed with [i] for i in [1:9]
    if arr is None:
        for i in tqdm(starts):
            s += recursive(list(map(int, i)))
        return s
    # print(len(arr))
    remain = max_d - len(arr)
    if remain == 6:
        return len(next_six[f"{arr[-2]}{arr[-1]}"])
    elif remain == 5:
        return next_five[f"{arr[-2]}{arr[-1]}"]
    if remain == 4:
        return next_four[f"{arr[-2]}{arr[-1]}"]
    elif remain == 3:
        return next_three[f"{arr[-2]}{arr[-1]}"]
    elif remain == 2:
        return next_two[f"{arr[-2]}{arr[-1]}"]
    elif remain == 1:
        return 10 - sum(arr[-2:])
    elif remain == 0:
        return 1
    else:
        for i in next_six[f"{arr[-2]}{arr[-1]}"]:
            s += recursive(arr + list(map(int, i)))
    return s


print(recursive())
