# Digital Root Clocks
import primesieve

cost = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
sam_total = 43927220

arrangements = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6]
}

total = 0

prev = None


def max_cost(a, b):
    if a is None:
        c = 0
        for d in [int(s) for s in str(b)]:
            c += cost[d]
        return c
    sa = [int(s) for s in str(a)[::-1]]
    sb = [int(s) for s in str(b)[::-1]]

    t = 0

    for i in range(0, len(sa)):
        if sa[i] != sb[i]:
            xa = arrangements[sa[i]]
            xb = arrangements[sb[i]]
            d = set(xa).difference(set(xb))
            s = set(xb).difference(set(xa))
            c = len(d) + len(s)
            t += c

    for i in range(len(sa), len(sb)):
        t += cost[sb[i]]

    return t


print(max_cost(11, 115))

primes = primesieve.primes(2*10**7)

for i in primes:
    if i > 10**7:
        c = max_cost(prev, i)
        total += max_cost(prev, i)
        prev = i

for s in str(primes[-1]):
    total += cost[int(s)]


print(sam_total - total)
