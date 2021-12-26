# ACM Contest Scoring
from collections import defaultdict

wrongs = defaultdict(int)
completed = set()
score = 0

l = input()
while l != "-1":
    t, p, c = l.split()
    if p not in completed:
        if c == "wrong":
            wrongs[p] += 1
        else:
            completed.add(p)
            score += int(t)
    l = input()

score += 20 * sum(v for k, v in wrongs.items() if k in completed)

print(len(completed), score)
