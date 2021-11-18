# Okvir

M, N = map(int, input().split())

U, L, R, D = map(int, input().split())

words = [input() for _ in range(M)]


def line(l, p):
    if p:
        print("#." * (l // 2), end="")
        if l % 2:
            print("#", end="")
    else:
        print(".#" * (l // 2), end="")
        if l % 2:
            print(".", end="")


pound = True
W = N + L + R
for _ in range(U):
    line(W, pound)
    print()
    pound = not pound

for w in words:
    line(L, pound)
    print(w, end="")
    if N % 2:
        line(R, not pound)
    else:
        line(R, pound)
    print()
    pound = not pound

for _ in range(D):
    line(W, pound)
    print()
    pound = not pound
