# ABC

vals = sorted(list(map(int, input().split())))
d = {"A": vals[0], "B": vals[1], "C": vals[2]}

order = input()

for a in order:
    print(d[a], end=" ")
