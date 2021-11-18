# ICPC Tutorial
from math import log


def custom_factorial(x, top, total=1):
    if x == 1:
        return total
    if total > top:
        return top + 1
    return custom_factorial(x-1, top, total * x)


m, n, t = map(int, input().split())

if t == 1:
    print("TLE" if custom_factorial(n, m) > m else "AC")
elif t == 2:
    print("TLE" if 2**n > m else "AC")
elif t == 3:
    print("TLE" if n**4 > m else "AC")
elif t == 4:
    print("TLE" if n**3 > m else "AC")
elif t == 5:
    print("TLE" if n**2 > m else "AC")
elif t == 6:
    print("TLE" if n * log(n, 2) > m else "AC")
elif t == 7:
    print("TLE" if n > m else "AC")
