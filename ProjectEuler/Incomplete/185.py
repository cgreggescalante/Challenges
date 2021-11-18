# Number Mind

guesses = []
with open("../Resources/guesses185.txt") as file:
    for line in file.readlines():
        line = line.strip().split(";")
        guesses.append([line[0].strip(), int(line[1][0])])

options = []
for d in range(len(guesses[0][0])):
    poss = set()
    for g in guesses:
        if g[1]:
            poss.add(g[0][d])
    options.append(poss)
    print(sorted(poss))


def rec_e():

