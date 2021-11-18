# Piece Of Cake!

n, h, v = map(int, input().split())

h = h if h > n / 2 else n - h
v = v if v > n / 2 else n - v

print(h * v * 4)
