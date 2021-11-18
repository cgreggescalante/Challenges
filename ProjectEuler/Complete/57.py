import sys
sys.setrecursionlimit(10**6)


def inverse(x):
    x[0], x[1] = x[1], x[0]

    return x


def add(x, n):
    x[0] += n * x[1]

    return x


def iter_outward(x, level):
    if level == 0:
        return x
    x = add(inverse(x), 2)

    return iter_outward(x, level - 1)


def continued(n):
    x = iter_outward([2, 1], n)
    return add(inverse(x), 1)


count = 0
for i in range(1000):
    frac = continued(i)

    if len(str(frac[0])) > len(str(frac[1])):
        count += 1

print(count)
