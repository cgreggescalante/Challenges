# Railroad

X, Y = map(int, input().split())

print("impossible" if (X * 2 + Y * 3) % 2 else "possible")
