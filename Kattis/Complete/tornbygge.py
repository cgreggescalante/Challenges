# Tower Construction

n = int(input())

arr = list(map(int, input().split()))

i = 1
towers = 1
current = arr[0]

while i < n:
    if arr[i] > current:
        towers += 1
    current = arr[i]
    i += 1

print(towers)
