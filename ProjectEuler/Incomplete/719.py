# Number Splitting
from math import sqrt

N = 10**12


def squares():
    a = 2
    while a * a <= N:
        yield a * a
        a += 1


def divide(n):
    sn = sqrt(n)
    arr = list(map(int, str(n)))

    for i in range(1, 2**(len(arr) - 1)):
        mapping = list(map(int, [a for a in format(i, "0" + str(len(arr) - 1) + "b")]))
        cpy = arr[:]
        splits = [cpy.pop(0)]
        for m in mapping:
            if m:
                splits.append(cpy.pop(0))
            else:
                splits[-1] *= 10
                splits[-1] += cpy.pop(0)

        if sum(splits) == sn:
            return True

    return False


it = squares()
total = 0

while True:
    try:
        n = next(it)

        if divide(n):
            total += n
            print(n, total)
    except StopIteration:
        break
