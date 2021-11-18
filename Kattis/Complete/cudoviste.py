# Cudoviste

R, C = map(int, input().split())

arr = [input() for _ in range(R)]

results = [0, 0, 0, 0, 0]

for i in range(C - 1):
    for j in range(R - 1):
        selection = arr[j][i:i + 2] + arr[j + 1][i:i + 2]
        if "#" not in selection:
            results[selection.count("X")] += 1

print('\n'.join(map(str, results)))
