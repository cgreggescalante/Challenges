# Semafori

N, L = map(int, input().split())

time = 0
pos = 0

for _ in range(N):
    D, R, G = map(int, input().split())

    time += D - pos
    pos = D

    cycle_pos = time % (R + G)

    if cycle_pos <= R:
        time += R - cycle_pos + 1

if time < L:
    time += L - time

print(time)
