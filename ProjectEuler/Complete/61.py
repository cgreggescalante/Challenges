# Cyclical Figurate Numbers


def triangle(n):
    return (n * (n + 1)) // 2


def square(n):
    return n * n


def pentagonal(n):
    return (n * (3 * n - 1)) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return (n * (5 * n - 3)) // 2


def octagonal(n):
    return n * (3 * n - 2)


def filter(options, path=None):
    if not path:
        for v in valids[options[-1]]:
            filter(options[:-1], [v])
        return

    if len(path) == 6 and path[0] // 100 == path[-1] % 100:
        print(path)
        print(sum(path))

    nexts = {}
    for o in options:
        nexts[o] = []
        for v in valids[o]:
            if v // 100 == path[-1] % 100 and v % 100 > 9:
                nexts[o].append(v)

    for n in nexts:
        os = options[:]
        os.remove(n)
        for x in nexts[n]:
            filter(os, path + [x])

valids = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

n = 0

while triangle(n) < 10000:
    t = triangle(n)
    if 10000 > t > 999:
        valids[0].append(t)
    t = square(n)
    if 10000 > t > 999:
        valids[1].append(t)
    t = pentagonal(n)
    if 10000 > t > 999:
        valids[2].append(t)
    t = hexagonal(n)
    if 10000 > t > 999:
        valids[3].append(t)
    t = heptagonal(n)
    if 10000 > t > 999:
        valids[4].append(t)
    t = octagonal(n)
    if 10000 > t > 999:
        valids[5].append(t)
    n += 1

filter([0, 1, 2, 3, 4, 5])
