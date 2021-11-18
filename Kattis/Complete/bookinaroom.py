# Booking a Room

r, n = map(int, input().split())

avail = {i: 0 for i in range(1, r+1)}

for _ in range(n):
    b = int(input())
    avail[b] = 1

avail = [a for a in avail if avail[a] == 0]

if not avail:
    print("too late")
else:
    print(avail[0])
