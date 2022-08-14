# Disc game prize fund

turns = 15


def play(turn=1, blues=0, n=1, d=1):
    if blues > turns / 2:
        return n, d

    if turn == turns + 1:
        return 0, 1

    bn, bd = play(turn + 1, blues + 1, n, d * (turn + 1))

    rn, rd = play(turn + 1, blues, n * turn, d * (turn + 1))

    tn = bn * rd + rn * bd
    td = bd * rd

    return tn, td


n, d = play()

print(d // n)
