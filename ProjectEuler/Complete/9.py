# Special Pythagorean Triplet

for a in range(1, 1000):
    a2 = a * a
    for b in range(a, 1000):
        c = 1000 - a - b
        if a2 + b * b == c * c:
            print(a * b * c)
            quit()
