# Quick Sort
import random

with open("../Resources/rosalind_qs.txt") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))


def quick_sort(arr, low=0, high=len(arr)-1):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        quick_sort(arr, low, i)
        quick_sort(arr, i + 2, high)


quick_sort(arr)

print(' '.join(map(str, arr)))
