# 2048

def left(board):
    nb = []
    for row in board:
        row = [a for a in row if a]
        i = 0
        while i < len(row) - 1:
            if row[i] == row[i+1]:
                row[i] *= 2
                row = row[:i+1] + row[i+2:]
            i += 1
        while len(row) < 4:
            row.append(0)
        nb.append(row)
    return nb


def right(board):
    board = [row[::-1] for row in board]
    board = left(board)
    return [row[::-1] for row in board]


def up(board):
    board = [[board[i][j] for i in range(4)] for j in range(4)]
    board = left(board)
    return [[board[i][j] for i in range(4)] for j in range(4)]


def down(board):
    board = [[board[i][j] for i in range(4)] for j in range(4)]
    board = [row[::-1] for row in board]
    board = left(board)
    board = [row[::-1] for row in board]
    return [[board[i][j] for i in range(4)] for j in range(4)]


board = [list(map(int, input().split())) for _ in range(4)]

dir = int(input())

if dir == 0:
    board = left(board)
elif dir == 1:
    board = up(board)
elif dir == 2:
    board = right(board)
else:
    board = down(board)

for row in board:
    print(' '.join(map(str, row)))
