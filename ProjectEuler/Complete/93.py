# Arithmetic Expressions
from itertools import permutations


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def evaluate(values):
    perms = permutations(values, 4)
    opps = [add, sub, mult, div]

    resultants = set()

    for vals in list(perms):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    try:
                        r1 = opps[i](vals[0], opps[j](vals[1], opps[k](vals[2], vals[3])))
                    except ZeroDivisionError:
                        r1 = -1
                    try:
                        r2 = opps[k](opps[i](vals[0], opps[j](vals[1], vals[2])), vals[3])
                    except ZeroDivisionError:
                        r2 = -1
                    try:
                        r3 = opps[k](opps[j](opps[i](vals[0], vals[1]), vals[2]), vals[3])
                    except ZeroDivisionError:
                        r3 = -1
                    try:
                        r4 = opps[j](opps[i](vals[0], vals[1]), opps[k](vals[2], vals[3]))
                    except ZeroDivisionError:
                        r4 = -1

                    for r in [r1, r2, r3, r4]:
                        resultants.add(r)

    i = 0
    while i + 1 in resultants:
        i += 1

    return i


top = 0
for a in range(1, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                l = evaluate([a, b, c, d])

                if l > top:
                    print(f"{l} : {a}{b}{c}{d}")
                    top = l
