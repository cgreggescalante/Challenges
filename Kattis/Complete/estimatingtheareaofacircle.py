# Estimating the Area of a Circle
import math

r, m, c = map(float, input().split())

while r + m + c > 0:
    print(r ** 2 * math.pi, r ** 2 * 4 * c / m)
    r, m, c = map(float, input().split())
