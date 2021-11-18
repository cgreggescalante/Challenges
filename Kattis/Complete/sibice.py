# Sibice

N, W, H = map(int, input().split())

max_length = ((W**2) + (H**2)) ** .5

for _ in range(N):
    if int(input()) > max_length:
        print("NE")
    else:
        print("DA")
