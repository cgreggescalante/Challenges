# Numbers for which no three consecutive digits have sum greater than a given value
from tqdm import tqdm

target = 20
checked = 0


def check(n):
    global checked
    checked += 1
    a = list(map(int, str(n)))[::-1]
    s = sum(a[:3])
    if s > 9:
        return 0
    for i in range(3, len(a)):
        s -= a[i - 3]
        s += a[i]
        if s > 9:
            return i - 3
    return -1


def valid():
    n = 10**(target-1)
    while n < 10**target:
        d = check(n)
        if d == -1:
            yield n
            n += 1
        else:
            n += 10 ** d
            if d > 0:
                n -= n % (10 ** (d - 1))


v = valid()
progress = tqdm(total=int(("900"*(target//3 + 1))[:target]))
s = 0
for i in v:
    progress.n = i
    progress.update()
    # print(i)
    s += 1
print(s)
print(f"Checked {checked} of {10**target-10**(target-1)} possible")
print(f"% Checked: {checked/(10**target-10**(target-1)):.3f}")

