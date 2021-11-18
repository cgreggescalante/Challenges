# Hyperexponentiation
import sys

sys.setrecursionlimit(2000)


def exponentiate(a, b):
    global t
    if b == 1:
        return a
    z = pow(a, exponentiate(a, b-1), 10**8)
    t.update(1)
    return z


print(exponentiate(1777, 1855))
