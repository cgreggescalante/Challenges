# Heap Sort
from tqdm import tqdm

with open("../Resources/rosalind_hs.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

for j in tqdm(range(n, 0, -1)):
    swap = True
    while swap:
        swap = False
        for i in range(j - 1, 0, -1):
            if arr[i] > arr[i // 2]:
                arr[i // 2], arr[i] = arr[i], arr[i // 2]
                swap = True

    arr[j - 1], arr[0] = arr[0], arr[j - 1]

print(' '.join(map(str, arr)))
