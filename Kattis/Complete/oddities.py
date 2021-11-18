# Oddities

N = int(input())

for _ in range(N):
    x = int(input())
    if x % 2:
        print(x, "is odd")
    else:
        print(x, "is even")
