# Right Triangles With Integer Coordinates


def check(x1, y1, x2, y2):
    x3 = x1 - x2
    y3 = y1 - y2
    if x1 * x2 + y1 * y2 == 0:
        return True
    if x1 * x3 + y1 * y3 == 0:
        return True
    if x2 * x3 + y2 * y3 == 0:
        return True
    return False


options = {}

limit = 51

for x in range(limit):
    for y in range(limit):
        if not (x == 0 and y == 0):
            for x1 in range(limit):
                for y1 in range(limit):
                    if not (x1 == 0 and y1 == 0) and not (x == x1 and y == y1) and check(x, y, x1, y1):
                        try:
                            a = options[f"{x} {y} {x1} {y1}"]
                        except KeyError:
                            try:
                                a = options[f"{x1} {y1} {x} {y}"]
                            except KeyError:
                                options[f"{x} {y} {x1} {y1}"] = 0

print(len(options))
