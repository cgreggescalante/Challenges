# Relocation

locations = {}

N, Q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(Q):
    a, b, c = map(int, input().split())

    if a == 1:
        arr[b - 1] = c
    else:
        print(abs(arr[b - 1] - arr[c - 1]))
