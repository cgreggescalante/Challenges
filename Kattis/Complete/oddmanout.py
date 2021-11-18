# Odd Man Out
from collections import defaultdict

n = int(input())

for i in range(n):
    g = int(input())
    d = defaultdict(int)
    arr = list(map(int, input().split()))
    for a in arr:
        d[a] += 1
    for k in d:
        if d[k] == 1:
            print(f"Case #{i+1}: {k}")
            break
