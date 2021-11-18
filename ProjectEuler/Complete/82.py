# Path Sum : Three Ways

directions = [[0, -1], [1, 0], [0, 1]]

with open('../Resources/matrix82.txt', 'r') as file:
    lines = file.readlines()

    matrix = [[int(i) for i in line.split(',')] for line in lines]

low = sum(matrix[0])


def calculate(i):
    new_row = []
    for j in range(len(matrix)):
        local_low = matrix[j][i] + matrix[j][i+1]

        c = j - 1
        current = matrix[j][i]
        while c > -1:
            current += matrix[c][i]
            if current + matrix[c][i+1] < local_low:
                local_low = current + matrix[c][i+1]
            c -= 1

        c = j + 1
        current = matrix[j][i]
        while c < len(matrix):
            current += matrix[c][i]
            if current + matrix[c][i + 1] < local_low:
                local_low = current + matrix[c][i + 1]
            c += 1

        new_row.append(local_low)

    for c in range(len(matrix)):
        matrix[c][i] = new_row[c]


for i in range(len(matrix[0]) - 2, -1, -1):
    calculate(i)

print(min([a[0] for a in matrix]))
