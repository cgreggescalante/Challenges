# Singular Integer Right Triangles

options = {}

m = 2
top = 2000000
options = {}

while True:
    end = 0
    for n in range(1, m):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n

        t = a + b + c
        if t > top:
            end = n
            break

        s = ' '.join(map(str, sorted([a, b, c])))
        try:
            options[t][s] = 0
        except KeyError:
            options[t] = {s: 0}

        x = 1
        while t * x < top:
            s = ' '.join(map(str, sorted([a * x, b * x, c * x])))
            try:
                options[t * x][s] = 0
            except KeyError:
                options[t * x] = {s: 0}
            x += 1
    if end == 1:
        break
    m += 1

c = 0
for t in options:
    if len(options[t]) == 1 and t <= 1500000:
        c += 1

print(c)
