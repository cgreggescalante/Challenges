# Social Running

N = int(input())

arr = [int(input()) for _ in range(N)]

m = 10**100

for i in range(N):
    d = arr[i] + arr[i - 2]
    if d < m:
        m = d

print(m)
