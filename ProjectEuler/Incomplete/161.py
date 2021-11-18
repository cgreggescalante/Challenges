# Triominoes
import copy

shapes = [
    [(0, 0), (0, 1), (1, 0)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (1, -1)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2)]
]

n, m = 2, 9

grid = [[0 for _ in range(n)] for _ in range(9)]


def rec_e(i, j, grid):
    if sum(sum(a) for a in grid) == m * m:
        print("full")
        return 1
    total = 0
    while i < m:
        while j < n:
            if grid[i][j] == 0:
                for s in shapes:
                    t = 0
                    new_grid = copy.deepcopy(grid)
                    for p in s:
                        if m > i + p[0] > -1 and n > j + p[1] > -1:
                            if new_grid[i + p[0]][j + p[1]] == 0:
                                new_grid[i + p[0]][j + p[1]] = 1
                                t += 1
                    if t == 3:
                        total += rec_e(i, j + 1, new_grid)
            j += 1
        j = 0
        i += 1
    print(grid)
    return total


print(rec_e(0, 0, grid))
