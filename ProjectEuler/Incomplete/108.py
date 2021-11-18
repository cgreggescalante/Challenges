# Diophantine Reciprocals I

n = 4
target = 1000
high = 0
high_n = 0


while high < target:
    n1 = 1 / n

    c = 0
    for x in range(n + 1, n * 2 + 1):
        y = x / (n1 * x - 1)
        if y == int(y):
            c += 1
    if c > high:
        print((n - high_n) / 8, n)
        high = c
        high_n = n

    n += 4
