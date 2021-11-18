# School Spirit

n = int(input())

arr = [int(input()) for _ in range(n)]

s = sum(arr[i] * (4 / 5) ** i for i in range(n))

print(s / 5)

t = 0

for i in range(n):
    x = 0
    for j in range(n):
        if j == i:
            continue
        if j > i:
            x += arr[j] * (4 / 5) ** (j - 1)
        else:
            x += arr[j] * (4 / 5) ** j
    t += x / 5

print(t / n)
