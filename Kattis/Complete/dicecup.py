# Dice Cup
from collections import defaultdict

N, M = map(int, input().split())

d = defaultdict(int)
m = []
mc = -1

for i in range(1, N+1):
    for j in range(1, M+1):
        d[i + j] += 1
        if d[i + j] > mc:
            mc = d[i + j]
            m = [i + j]
        elif d[i + j] == mc:
            m.append(i + j)

print('\n'.join(map(str, m)))
