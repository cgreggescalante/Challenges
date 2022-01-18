# Binary Search

with open("../Resources/rosalind_bins.txt", "r") as file:
    lines = file.readlines()
    n = int(lines[0])
    m = int(lines[1])
    arr = list(map(int, lines[2].split()))
    targets = list(map(int, lines[3].split()))

for target in targets:
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        l, r = left, right
        if arr[mid] > target:
            right = mid
        elif arr[mid] < target:
            left = mid
        else:
            print(mid + 1, end=" ")
            break
        if mid == l:
            print(-1, end=" ")
            break
