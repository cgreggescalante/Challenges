# The Amazing Human Cannonball
from math import cos, radians, sin

n = int(input())

for _ in range(n):
    velocity, angle, distance, h1, h2 = map(float, input().split())

    time = distance / (cos(radians(angle)) * velocity)

    height = velocity * time * sin(radians(angle)) - (9.81 * time ** 2) / 2

    print("Safe" if h1 + 1 < height < h2 - 1 else "Not Safe")
