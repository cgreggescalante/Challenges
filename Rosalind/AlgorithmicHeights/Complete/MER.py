# Merge Two Sorted Arrays

with open("../Resources/rosalind_mer.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))
    m = int(file.readline())
    arr1 = list(map(int, file.readline().split()))

out = []

while arr and arr1:
    if arr[0] < arr1[0]:
        out.append(arr.pop(0))
    else:
        out.append(arr1.pop(0))

if arr:
    out.extend(arr)

if arr1:
    out.extend(arr1)

print(' '.join(map(str, out)))
