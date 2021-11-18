# Optimum Polynomial

def u():
    n = 0
    while True:
        yield 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
        n += 1


def n3():
    n = 1
    while True:
        yield n**3
        n += 1


seq = u()
vs = [next(seq) for _ in range(100)]
print(vs)
for _ in range(10):
    vs = [vs[i+1] - vs[i] for i in range(len(vs) - 1)]
    print(vs)
