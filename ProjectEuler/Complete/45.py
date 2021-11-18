tri = []
pent = []
hex = []

for n in range(100000):
    tri.append(n * (n + 1) // 2)
    pent.append(n * (3 * n - 1) // 2)
    hex.append(n * (2 * n - 1))

for i in tri:
    if i > max(pent):
        break
    if i in pent and i in hex:
        print(i)