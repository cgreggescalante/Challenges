# Mjehuric

arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(' '.join(map(str, arr)))
