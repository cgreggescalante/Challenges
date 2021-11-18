# Roots on the Rise

def func(k, x):
    return (k / x) ** 2 * (k + x * x) - k * x


def sumk(n):
    for k in range(1, n):
