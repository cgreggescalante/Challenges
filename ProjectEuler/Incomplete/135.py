# Same Differences
from math import sqrt


def func(x, n):
    return (1 / 5) * (-3 * x + sqrt(-5 * n + 4 * x ** 2))


n = 27
b = int(sqrt(n) // 2 + 1)
print(b)

while True:
    x = sqrt(4 * b * b - n) + 3 * b
    if x == int(x):
        x = int(x)
        print(x, x - b, x - b - b)
    b += 1
