# Largest Exponent

from math import log

with open("C:\\Users\\Conor\\PycharmProjects\\EulerStuff\\Resources\\BaseExp99.txt") as numbers:
    numbers = numbers.readlines()
    max_val = 0
    max_index = -1
    for n in range(len(numbers)):
        parts = numbers[n].split(",")
        val = int(parts[1]) * log(int(parts[0]))
        if val > max_val:
            max_val = val
            max_index = n
    print(max_index + 1)
