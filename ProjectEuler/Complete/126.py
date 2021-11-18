# Cuboid Layers

count = 0
n = 15352
while count != 1000:
    a = 1
    count = 0

    while a * 4 + 2 <= n:
        for b in range(1, a + 1):
            for c in range(1, b + 1):
                if 2 * (a * b + a * c + c * b) > n:
                    break

                core = a * b
                current = 2 * (a + b)
                total = core

                while total * 2 + current * c < n:
                    total += current
                    current += 4

                if total * 2 + current * c == n:
                    count += 1

            if 2 * (a * b + a + b) > n:
                break

        a += 1

    if count > 1000:
        print(n, count)
    n += 10

print(n)