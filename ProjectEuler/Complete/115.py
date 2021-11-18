# Counting Block Combinations II

known = {}


def options(m, row_length):
    c = 0
    for tile_length in range(m, row_length + 1):
        c += row_length - tile_length + 1
        for remain in range(row_length - tile_length - 1, m - 1, -1):
            try:
                c += known[remain]
            except KeyError:
                a = options(m, remain)
                known[remain] = a
                c += a
    return c


length = 50

while True:
    c = options(50, length) + 1
    if c > 1000000:
        print(length)
        break
    length += 1
