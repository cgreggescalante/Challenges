# Perfect Square Collection

check = {}

for i in range(1, 10000):
    check[i * i] = 0

for a in range(1, 10000):
    a2 = a * a
    for x in range(a2 // 2, a2):
        y = a2 - x
        try:
            l = check[x - y]
            try:
                for b in range(a+1, 10000):

        except KeyError:
            pass
