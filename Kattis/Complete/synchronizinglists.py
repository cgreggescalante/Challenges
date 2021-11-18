# Synchronizing Lists

n = int(input())

while n > 0:
    a = [int(input()) for _ in range(n)]
    sa = sorted(a)
    b = [int(input()) for _ in range(n)]
    sb = sorted(b)

    for i in a:
        idx = sa.index(i)
        print(sb[idx])

    print()
    n = int(input())
