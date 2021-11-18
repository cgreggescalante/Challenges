# Server

n, T = map(int, input().split())

arr = list(map(int, input().split()))
c = 0

for i in arr:
    if T < i:
        break
    T -= i
    c += 1

print(c)
