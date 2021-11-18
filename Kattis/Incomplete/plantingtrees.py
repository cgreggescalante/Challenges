# Planting Trees

N = int(input())

arr = sorted(list(map(int, input().split())))[::-1]

ends = 1

for i in range(len(arr)):
    if i + arr[i] + 2 > ends:
        ends = arr[i] + i + 2

print(ends)
