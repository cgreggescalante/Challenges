# Zamka

L = int(input())
D = int(input())
X = int(input())

for N in range(L, D + 1):
    if X == sum(map(int, str(N))):
        print(N)
        break

for M in range(D, L - 1, -1):
    if X == sum(map(int, str(M))):
        print(M)
        break
