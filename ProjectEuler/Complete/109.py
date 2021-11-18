# Darts

singles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25]
doubles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 50]
trebles = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

count = 0


def options(n, middle=True):

    if not middle:
        opts = []

        if n in singles:
            opts.append("S" + str(n))
        if n in doubles:
            opts.append("D" + str(n // 2))
        if n in trebles:
            opts.append("T" + str(n // 3))
        return opts

    opts = {}

    for s in singles:
        if s == n:
            opts["S" + str(s)] = 0
            break
        if s < n:
            opts["S" + str(s)] = options(n - s, False)
    for d in doubles:
        if d == n:
            opts["D" + str(d // 2)] = 0
            break
        if d < n:
            opts["D" + str(d // 2)] = options(n - d, False)
    for t in trebles:
        if t == n:
            opts["T" + str(t // 3)] = 0
            break
        if t < n:
            opts["T" + str(t // 3)] = options(n - t, False)

    return opts


for target in range(2, 100):
    for double in doubles:
        if double == target:
            count += 1
            break
        if double < target:
            os = {}

            remain = target - double
            for key, value in options(remain).items():
                res = []
                if value == 0:
                    res = [0]
                    count += 1
                else:
                    for i in value:
                        if i not in os or key == i:
                            res.append(i)
                            count += 1
                if len(res) > 0:
                    os[key] = res

print(count)