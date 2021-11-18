# Weak Vertices
from itertools import combinations

n = int(input())

while n > 0:
    arr = []

    for i in range(n):
        conn = list(map(int, input().split()))
        arr.append({j for j in range(n) if conn[j]})

    for v in range(n):
        found = False
        for a, b in combinations(arr[v], 2):
            if a in arr[b]:
                found = True
                break
        if not found:
            print(v, end=" ")
    print()
    n = int(input())
