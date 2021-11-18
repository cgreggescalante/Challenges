# Integer Partition Equations
from mpmath import mpf, log, root, power, mp

mp.dps = 200


def find_t(k):
    return log(root(k + mpf(1/4), 2) + mpf(1/2), 2)


total = mpf(1)
perfect = mpf(1)
check = {
    5: mpf(1),
    6: mpf(1)/mpf(2),
    10: mpf(1)/mpf(2),
    15: mpf(2)/mpf(3),
    20: mpf(1)/mpf(2),
    25: mpf(1)/mpf(2),
    30: mpf(2)/mpf(5),
    180: mpf(1)/mpf(4),
    185: mpf(3)/mpf(13)
}

print(2, 1, 1)
m = 3
while perfect / total >= 1/12345:
    t = find_t(m)
    four, two = power(4, t), power(2, t)
    if int(four) == four and int(two) == two and four - two == m:
        # print(m)
        total += 1
        if int(t) == t:
            print(m, int(t), perfect / total)
            perfect += 1
        if m in check:
            try:
                assert check[m] == perfect / total
            except AssertionError:
                print(f"m = {m}")
                print(f"{check[m]} != {perfect / total}")
                print(type(check[m]), type(perfect / total))

    m += 1

print(m, total)
