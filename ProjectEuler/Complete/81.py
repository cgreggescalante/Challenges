file = open('Resources/Matrix81.txt', 'r').readlines()

matrix = []

for line in file:
    matrix.append([int(a) for a in line.split()])

diag = 157

while diag >= 0:
    for x in range(80):
        for y in range(80):
            if x + y == diag:
                if x == 79:
                    matrix[y][x] += matrix[y + 1][x]
                elif y == 79:
                    matrix[y][x] += matrix[y][x + 1]
                else:
                    added = min(matrix[y][x + 1], matrix[y + 1][x])
                    matrix[y][x] += added
    diag -= 1

print(matrix[0][0])
