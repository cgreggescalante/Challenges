grid = []
for i in range(20):
    row = []
    for j in range(20):
        row.append(0)
    row.append(1)
    grid.append(row)
row = []
for i in range(21):
    row.append(1)
grid.append(row)

for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        grid[i][j] = grid[i+1][j] + grid[i][j+1]

print(grid[0][0])