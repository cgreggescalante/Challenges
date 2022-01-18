# Merge Sort

with open("../Resources/rosalind_ms.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    a, b = arr[:len(arr) // 2], arr[len(arr) // 2:]
    a, b = merge_sort(a), merge_sort(b)
    out = []
    while a and b:
        if a[0] < b[0]:
            out.append(a.pop(0))
        else:
            out.append(b.pop(0))
    if a:
        out.extend(a)
    if b:
        out.extend(b)
    return out


print(' '.join(map(str, merge_sort(arr))))
