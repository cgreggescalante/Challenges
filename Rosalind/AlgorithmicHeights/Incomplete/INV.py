# Counting Inversions

with open("../Resources/rosalind_inv.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

c = 0

for i in range(n):
    for j in range(i + 1, n):
        c += arr[i] > arr[j]

print(c)
