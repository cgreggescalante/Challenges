# Temperature Confusion
from math import gcd

n, d = map(int, input().split("/"))

n -= 32 * d
n *= 5
d *= 9

g = gcd(n, d)
while g > 1:
    n //= g
    d //= g
    g = gcd(n, d)

print(f"{n}/{d}")
