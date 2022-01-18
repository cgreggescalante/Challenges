# Median
import random

with open("../Resources/rosalind_med.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))
    k = int(file.readline())


while len(arr) > k:
    r = random.choice(arr)
    a = []
    e = []
    b = []
    for c in arr:
        if c < r:
            a.append(c)
        elif c == r:
            e.append(c)
        else:
            b.append(c)
    if k <= len(a):
        arr = a
    elif k <= len(e) + len(a):
        arr = e
        k -= len(a)
    else:
        arr = b
        k -= len(a) + len(e)

print(arr[0])
