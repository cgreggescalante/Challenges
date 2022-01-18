# 3SUM

with open("../Resources/rosalind_3sum.txt", "r") as file:
    k, n = map(int, file.readline().split())
    for _ in range(k):
        arr = list(map(int, file.readline().split()))
        s = set(arr)
        found = False
        for p in range(n):
            for q in range(p + 1, n):
                if -(arr[p] + arr[q]) in s:
                    print(p + 1, q + 1, arr.index(-(arr[p] + arr[q])) + 1)
                    found = True
                    break
            if found:
                break
        if not found:
            print(-1)
