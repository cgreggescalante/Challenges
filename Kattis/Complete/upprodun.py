# Arrangement

N = int(input())
M = int(input())

while (M / N) % 1 > 0:
    print((M // N + 1) * "*")
    M -= (M // N + 1)
    N -= 1

while M > 0:
    print((M // N) * "*")
    M -= M // N
    N -= 1
