# Misa
import copy

R, S = map(int, input().split())


def count(grid):
    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                if i < len(grid) - 1:
                    c += grid[i + 1][j]
                if j < len(grid[0]) - 1:
                    c += grid[i][j+1]
                if j > 0 and i < len(grid) - 1:
                    c += grid[i+1][j-1]
                if i < len(grid) - 1 and j < len(grid[0]) - 1:
                    c += grid[i+1][j+1]
    return c


arr = []

for _ in range(R):
    line = [a for a in input()]
    for i in range(S):
        line[i] = int(line[i] == "o")
    arr.append(line)

m = count(arr)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            dupe = copy.deepcopy(arr)
            dupe[i][j] = 1
            c = count(dupe)
            if c > m:
                m = c

print(m)
