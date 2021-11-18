# Counting Rectangles


def count(width, height):
    h = (height ** 2 - height) / 2 + height
    w = (width ** 2 - width) / 2 + width

    return h * w


target = 2000000
closest_count = 1
closest_dims = [1, 1]

width = 1
height = 1

c = count(width, height)

while count(width, 1) < target:
    while c < target:
        c = count(width, height)

        if abs(target - c) < abs(target - closest_count):
            closest_count = c
            closest_dims = [width, height]
            print(closest_dims, closest_count)

        height += 1
    width += 1
    height = 1
    c = count(width, height)

print(closest_dims[0] * closest_dims[1])
