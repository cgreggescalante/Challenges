# Skocimis

a, b, c = map(int, input().split())

m = 0

while a < b - 1 or b < c - 1:
    if b - a > c - b:
        c = b
        b = a + 1
    else:
        a = b
        b = c - 1
    m += 1

print(m)
