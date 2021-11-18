p = 120
big = 0


for p in range(1001):
    provenC = []
    for a in range(1, p):
        for b in range(1, p-a):
            c = p - a - b
            if a**2 + b**2 == c**2 and c not in provenC:
                provenC.append(c)
                #print([a, b, c])
    if len(provenC) > big:
        big = len(provenC)
        print(p, big)