# Reciprocal Cycles

from decimal import *

getcontext().prec = 8000

longest = 0
longest_d = 0

for d in range(1, 1000):
    num = Decimal(1) / Decimal(d)
    s = str(num)[2:]

    rep = 0

    if len(s) > 90:
        repeats = False
        start = 0
        while not repeats and start < 10:
            for i in range(1, 2000):
                sequence = s[start:i+start]
                if sequence == s[i+start:i+i+start] == s[i+i+start:i+i+i+start]:
                    repeats = True
                    rep = i
                    break
            start += 1

        if rep > 0 and repeats:
            if rep > longest:
                longest = rep
                longest_d = d
                print(rep)
                print(s[start:start+rep+rep])
                print(d)
                print()
