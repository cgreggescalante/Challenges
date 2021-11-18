# Trik

cups = [1, 0, 0]

for c in input():
    if c == "A":
        cups[0], cups[1] = cups[1], cups[0]
    elif c == "B":
        cups[1], cups[2] = cups[2], cups[1]
    else:
        cups[0], cups[2] = cups[2], cups[0]

print(cups.index(1) + 1)
