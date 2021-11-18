# Matrix Sum

test_matrix = [
    [7, 53, 183, 439, 863],
    [497, 383, 563, 79, 973],
    [287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303]
]

s = 0


def find_sum(matrix, c=0, current=0):
    global s
    if len(matrix) == 0:
        if current > s:
            s = current
            print(s)
        return
    if current + row_maxes[c] < s:
        return

    for i in range(len(matrix)):
        nc = current + matrix[0][i]
        nm = [[matrix[a][b] for a in range(1, len(matrix))] for b in range(len(matrix)) if b != i]
        find_sum(nm, c+1, nc)

matrix = []
row_maxes = []

with open("../Resources/matrix345.txt", "r") as file:
    lines = file.readlines()
    for l in lines:
        matrix.append(list(map(int, l.split())))
        row_maxes.append(max(matrix[-1]))

s = sum([matrix[i][i] for i in range(len(matrix))])
print(s)
row_maxes = [sum(row_maxes[i:]) for i in range(len(row_maxes))]
print(row_maxes)
find_sum(matrix)
