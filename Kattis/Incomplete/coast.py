# Coast Length

N, M = map(int, input().split())

grid = [input() for _ in range(N)]

l = 0

for i in range(N):
    for j in range(M):
        if grid[i][j]:
            if i == 0 or grid[i-1][j] == 0:
                l += 1
            if j == 0 or grid[i][j-1] == 0:
                l += 1
            if j + 1 == M or grid[i][j+1] == 0:
                l += 1
            if i + 1 == N or grid[i+1][j] == 0:
                l += 1

print(l)
