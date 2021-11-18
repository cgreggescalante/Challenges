# Mia

a, b, c, d = map(int, input().split())

while a and b and c and d:
    p1, p2, = 0, 0
    mia1 = a == 1 and b == 2 or b == 1 and a == 2
    mia2 = c == 1 and d == 2 or d == 1 and c == 2

    d1 = a * 11 if a == b else 0
    d2 = c * 11 if c == d else 0

    a, b = sorted([a, b])
    c, d = sorted([c, d])
    r1 = b * 10 + a
    r2 = d * 10 + c

    if mia1 and not mia2:
        print("Player 1 wins.")
    elif mia2 and not mia1:
        print("Player 2 wins.")
    elif mia1 and mia2:
        print("Tie.")
    elif d1 > d2:
        print("Player 1 wins.")
    elif d2 > d1:
        print("Player 2 wins.")
    elif d1 == d2 and d1:
        print("Tie.")
    elif r1 > r2:
        print("Player 1 wins.")
    elif r2 > r1:
        print("Player 2 wins.")
    else:
        print("Tie.")
    a, b, c, d = map(int, input().split())
