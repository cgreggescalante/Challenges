# Near Power Sums
from collections import defaultdict

from tqdm import tqdm


def power_sum(arr: list, k: int) -> int:
    return sum(a ** k for a in arr)


def is_power_sum(n: int) -> bool:
    # print(n)
    k = 2
    arr = [a for a in map(int, str(n)) if a > 0]
    s = 0
    prev = 0
    while s < n + 1:
        s = power_sum(arr, k)
        if s == prev:
            break
        prev = s
        k += 1
        if s == n + 1 or s == n - 1:
            return True
    return False


def S(d: int) -> int:
    total = 0
    for i in range(2, 10**d):
        if is_power_sum(i):
            print(i)
            total += i
    return total


print(S(16))

