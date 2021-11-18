# Square Laminae

tiles = 1000000
side = 3
count = 0

while True:
    inner = side - 2

    if side * 4 - 4 > tiles:
        break

    while inner > 0:
        if side ** 2 - inner ** 2 <= tiles:
            count += 1
        else:
            break
        inner -= 2

    side += 1

print(count)
