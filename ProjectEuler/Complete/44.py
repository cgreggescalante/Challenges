# Pentagon Numbers

pentagons = []
pents = {}


def p(n):
    return n * (3 * n - 1) // 2


min_d = 5482660

k = 1

while True:
    pk = p(k)
    pentagons.append(pk)
    pents[pk] = 0

    for j in pentagons[:-1]:
        try:
            a = pents[pk - j]
            s = pk + j
            n = 0
            c = 0
            while n < s:
                c += 1
                n = p(c)
                if n == s:
                    print()
                    print(pk, j)
                    print(s, c)
                    print(pk - j)
        except KeyError:
            pass
    k += 1
