# Recount
from collections import defaultdict

d = defaultdict(lambda: 0)

line = input()

while line != "***":
    d[line] += 1
    line = input()

top = max(d.values())
winners = [a for a in d if d[a] == top]

if len(winners) == 1:
    print(winners[0])
else:
    print("Runoff!")
