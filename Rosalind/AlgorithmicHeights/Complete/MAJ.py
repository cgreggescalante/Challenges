# Majority Element

with open("../Resources/rosalind_maj.txt", "r") as file:
    k, n = map(int, file.readline().split())
    for _ in range(k):
        arr = list(map(int, file.readline().split()))
        c = {a: arr.count(a) for a in set(arr)}
        found = False
        for a, v in c.items():
            if v > n / 2:
                print(a, end=" ")
                found = True
        if not found:
            print(-1, end=" ")
