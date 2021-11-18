file = open('Resources/Triangle67.txt', 'r').readlines()
triangle = []

for line in file:
    line = line[:-1]
    triangle.append([int(a) for a in line.split()])

for row in range(98, -1, -1):
    for i in range(row + 1):
        triangle[row][i] += max(triangle[row + 1][i], triangle[row + 1][i+1])

print(triangle[0][0])
