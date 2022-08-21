# Digital Root Sums of Factorizations
from collections import defaultdict

from tqdm import tqdm


def digital_root_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s < 10:
        return s
    return digital_root_sum(s)


def max_drs(t):
    return sum(map(digital_root_sum, t))


target = 1000000

mdrs = defaultdict(int)


def add_factor(factors, prod):
    if prod >= target:
        return
    d = max_drs(factors)
    if d > mdrs[prod]:
        mdrs[prod] = d
    for i in range(factors[-1], target // prod + 1):
        add_factor(factors + (i,), prod * i)


for f in tqdm(range(2, target)):
    add_factor((f,), f)

print(sum(mdrs.values()))
