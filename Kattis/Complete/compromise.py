# Best Compromise

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    arr = [0 for _ in range(m)]
    for _ in range(n):
        a = list(map(int, input()))
        for i in range(m):
            arr[i] += a[i]
    print(''.join([str(int(a / n > .5)) for a in arr]))
