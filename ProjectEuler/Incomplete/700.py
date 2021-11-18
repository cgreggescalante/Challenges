# Eulercoin
from tqdm import tqdm

a = 1504170715041707
m = 4503599627370517

coins = []
smallest = 10**20

t = tqdm(range(m // 10000000))
for n in range(1, m):
    if n % 10000000 == 0:
        t.update(n // 10000000)
    b = (a * n) % m
    if b < smallest:
        smallest = b
        coins.append(b)
        print(len(coins), n, b, sum(coins))
    n += 1

print(sum(coins))
