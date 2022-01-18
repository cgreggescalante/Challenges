# Building a Heap

with open("../Resources/rosalind_hea.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

swap = True
while swap:
    swap = False
    for i in range(n, 2, -1):
        while i > 1:
            if arr[i - 1] > arr[i // 2 - 1]:
                arr[i // 2 - 1], arr[i - 1] = arr[i - 1], arr[i // 2 - 1]
                swap = True
            else:
                break
            i //= 2

print(' '.join(map(str, arr)))
