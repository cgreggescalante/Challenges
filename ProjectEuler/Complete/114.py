# Counting Block Combinations

length = 50

known = {}


def options(length):
    c = 0
    for l in range(3, length + 1):
        c += length - l + 1
        for remain in range(length - l - 1, 2, -1):
            try:
                c += known[remain]
            except KeyError:
                a = options(remain)
                known[remain] = a
                c += a
    return c


print(options(length) + 1)
