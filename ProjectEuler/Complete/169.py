# Exploring the number of different ways a number can be expressed as a sum of powers of 2

known = {}


def rec_e(n):
    if n in known:
        return known[n]
    c = 0
    for i in range(3):
        if n - i == 0:
            c += 1
            continue
        if (n - i) % 2 == 0:
            c += rec_e((n - i) // 2)
    known[n] = c
    return c


print(rec_e(10**25))
