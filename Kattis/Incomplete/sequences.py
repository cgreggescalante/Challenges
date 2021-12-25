# 0-1 Sequences

sequence = input()
qs = [i for i, a in enumerate(sequence) if a == "?"]

if len(qs):
    c = 0
    for a in range(2 ** len(qs)):
        mask = bin(a)[2:].rjust(len(qs), "0")
        sc = sequence[:]
        for m in mask:
            sc = sc.replace("?", m, 1)
        while sc and "1" in sc:
            if sc.endswith("1"):
                sc = sc[:-1]
            else:
                f = sc.rfind("1")
                c += len(sc) - f - 1
                sc = sc[:f] + sc[f + 1:]
    print(c)
    quit()

print(0)
