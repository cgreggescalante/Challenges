# Maximum product of parts
from math import log


def m(n):
    k = 1
    top = 0
    top_k = 0
    while True:
        try:
            log_x = k * log(n / k)
        except OverflowError:
            print(f"{n} / {k} ^ {k}")
            quit()
        if log_x > top:
            top = log_x
            top_k = k
        else:
            break
        k += 1
    return top_k


def d(n):
    k = m(n)
    while k % 2 == 0:
        k //= 2
    while k % 5 == 0:
        k //= 5
    if n % k == 0:
        return -n
    return n


total = 0
for n in range(5, 10001):
    total += d(n)
print(total)
