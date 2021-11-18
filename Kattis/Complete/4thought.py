# 4 thought

cases = {}

operators = ["+", "-", "*", "//"]


def passer(val):
    return val


for a in operators:
    for b in operators:
        for c in operators:
            exec(f"res = passer(4{a}4{b}4{c}4)")
            cases[res] = f"4 {a} 4 {b} 4 {c} 4".replace("//", "/")

m = int(input())

for _ in range(m):
    n = int(input())
    if n in cases:
        print(cases[n], "=", n)
    else:
        print("no solution")
