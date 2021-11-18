# Warehouse

T = int(input())

for _ in range(T):
    N = int(input())
    toys = {}

    for _ in range(N):
        toy, count = input().split()
        if toy in toys:
            toys[toy] += int(count)
        else:
            toys[toy] = int(count)

    toys = {k: toys[k] for k in sorted(toys)}
    print(len(toys))
    for k in sorted(toys, key=toys.get, reverse=True):
        print(k, toys[k])
