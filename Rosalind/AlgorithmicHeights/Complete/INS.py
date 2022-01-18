# Insertion Sort

with open("../Resources/rosalind_ins.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

c = 0

for i in range(n):
    k = i
    while k > 0 and arr[k] < arr[k - 1]:
        arr[k - 1], arr[k] = arr[k], arr[k - 1]
        c += 1
        k -= 1

print(c)
