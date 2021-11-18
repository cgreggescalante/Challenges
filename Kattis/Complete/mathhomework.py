# Math Homework

a, b, c, l = map(int, input().split())

legs = [a, b, c]
coef = [0, 0, 0]

i = -1
poss = False

while True:
    x = legs[0] * coef[0] + legs[1] * coef[1] + legs[2] * coef[2]
    while x < l:
        coef[i] += 1
        x = legs[0] * coef[0] + legs[1] * coef[1] + legs[2] * coef[2]
    if x == l:
        poss = True
        print(" ".join(map(str, coef)))
    if coef[1] * legs[1] > l:
        coef[0] += 1
        coef[1] = 0
    else:
        coef[1] += 1
        coef[2] = 0
    if coef[0] * legs[0] > l:
        break

if not poss:
    print("impossible")
