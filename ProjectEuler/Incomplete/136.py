# Singleton difference

target = 100


def val(x, d):
    return 6 * x * d - 5 * d**2 - x**2


def print_terms(x, d):
    print(f"{x} {x - d} {x - 2 * d}")


d = 1
while True:
    print(d)
    x = 2 * d + 1
    while True:
        v = val(x, d)
        if v == 20:
            print_terms(x, d)
            break
        elif v < 20:
            break
        x += 1
    d += 1
