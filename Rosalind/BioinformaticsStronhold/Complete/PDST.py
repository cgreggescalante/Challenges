# Creating a Distance Matrix
from Rosalind.FASTALoader import load

strings = [a for a in load('../Resources/rosalind_pdst.txt').values()]

matrix = []

for i in range(len(strings)):
    matrix.append([])
    for j in range(len(strings)):
        if i == j:
            matrix[i].append(0)
        else:
            c = 0
            for k in range(len(strings[i])):
                if strings[i][k] != strings[j][k]:
                    c += 1
            matrix[i].append(c / len(strings[i]))

for i in matrix:
    print(' '.join([str(a) for a in i]))
