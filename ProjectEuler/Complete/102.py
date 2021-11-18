# Triangle Containment


def subtract(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def cross_product(a, b):
    return [0, 0, a[0] * b[1] - a[1] * b[0]]


def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def same_side(p2, a, b):
    p1 = [0, 0, 0]
    c1 = cross_product(subtract(b, a), subtract(p1, a))
    c2 = cross_product(subtract(b, a), subtract(p2, a))

    return dot_product(c1, c2) >= 0


def encapsulates_origin(a, b, c):
    return same_side(a, b, c) and same_side(b, a, c) and same_side(c, a, b)


with open("C:\\Users\\Conor\\PycharmProjects\\EulerStuff\\Resources\\triangles102.txt", 'r') as file:
    triangles = file.readlines()
    total = 0
    for t in triangles:
        points = [int(a) for a in t.split(",")]
        total += encapsulates_origin([points[0], points[1], 0], [points[2], points[3], 0], [points[4], points[5], 0])

    print(total)
