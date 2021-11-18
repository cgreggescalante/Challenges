# Powers of Two
from tqdm import tqdm

L = "123"
N = 678910


precision = 1000
p = 2 ** 90
power = 90
c = 0

increase = 0
maps = {
    0: 196,
    1: 93,
    2: 196
}

t = tqdm(range(N))

while True:

    while len(str(p)) > 1000:
        p = p // 10

    if str(p)[:len(L)] == L:
        c += 1
        t.update()
        increase = 0
        if c == N:
            break

    if increase > 2:
        print("Failed")
        print(increase)
        break

    p *= 2**maps[increase]
    power += maps[increase]

    increase += 1

print(power)
