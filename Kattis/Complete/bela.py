# Bela

scoring = {
    'A': [11, 11],
    'K': [4, 4],
    'Q': [3, 3],
    'J': [20, 2],
    'T': [10, 10],
    '9': [14, 0]
}

for i in range(9):
    scoring[str(i)] = [0, 0]

N, B = input().split()

N = int(N)

s = 0

for _ in range(4 * N):
    l = input()

    if l[1] == B:
        s += scoring[l[0]][0]
    else:
        s += scoring[l[0]][1]

print(s)
