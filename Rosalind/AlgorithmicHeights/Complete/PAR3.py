# 3-Way Partition

with open("../Resources/rosalind_par3.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

v = arr[0]
a = []
e = []
b = []
for c in arr[1:]:
    if c < v:
        a.append(c)
    elif c == v:
        e.append(c)
    else:
        b.append(c)

print(' '.join(map(str, a + e + [v] + b)))
