from tqdm import tqdm

starts = set()
nexts = {}

for a in range(10):
    for b in tqdm(range(10 - a)):
        v = int(f"{a}{b}")
        nexts[v] = set()
        for c in range(10 - a - b):
            for d in range(10 - b - c):
                for e in range(10 - c - d):
                    for f in range(10 - d - e):
                        for g in range(10 - e - f):
                            for h in range(10 - f - g):
                                for i in range(10 - g - h):
                                    for j in range(10 - h - i):
                                        if a:
                                            starts.add(int(f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}"))

                                        for k in range(10 - i - j):
                                            for l in range(10 - j - k):
                                                nexts[v].add(int(f"{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}"))

for k in nexts:
    nexts[k] = len(nexts[k])

total = 0
for s in tqdm(starts):
    e = s % 100
    total += nexts[e]

print(total)
