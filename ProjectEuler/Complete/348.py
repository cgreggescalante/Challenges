# Sum of a Square and a Cube

square_check = {}

for a in range(1, 100000):
    square_check[a*a] = 0

cubes = [a*a*a for a in range(1, 1000)]
max_cube = 999**3


def check(n):
    if n > max_cube:
        print(n)
        quit()
    if n > 99999*99999:
        print(n)
        quit()
    matches = 0
    for cube in cubes:
        if cube > c:
            break
        diff = c - cube
        try:
            a = square_check[diff]
            matches += 1
        except KeyError:
            pass
        if matches > 4:
            return matches

    return matches


d = 2
total = 0
count = 0

while True:
    for n in range(10**(d-2), 10**(d-1)):
        s = str(n)
        c = int(s + s[::-1])
        if check(c) == 4:
            print(c)
            count += 1
            total += c
            if count == 5:
                print(total)
                quit()

    for n in range(10**(d-1), 10**d):
        s = str(n)
        c = int(s + s[:-1][::-1])
        if check(c) == 4:
            print(c)
            count += 1
            total += c
            if count == 5:
                print(total)
                quit()

    d += 1