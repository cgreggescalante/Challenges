# Tetris

configs = [
    [[0], [0, 0, 0, 0]],
    [[0, 0]],
    [[1, 1, 0], [0, 1]],
    [[0, 1, 1], [1, 0]],
    [[0, 0, 0], [1, 0], [0, 1, 0], [0, 1]],
    [[0, 0, 0], [0, 0], [1, 0, 0], [0, 2]],
    [[0, 0, 0], [2, 0], [0, 0, 1], [0, 0]]
]

C, P = map(int, input().split())

arr = list(map(int, input().split()))

count = 0

for arrangement in configs[P - 1]:
    for i in range(C - len(arrangement) + 1):
        s = {a + b for a, b in zip(arr[i:i+len(arrangement)], arrangement)}
        count += len(s) == 1

print(count)
