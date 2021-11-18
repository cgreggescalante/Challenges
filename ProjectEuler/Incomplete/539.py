# Odd elimination
from tqdm import tqdm

target = 3
total = 1
known = {1: 0, 2: 1}
check = {
    3: 268271,
    4: 26096543,
    5: 2133304431
}


def rec(n):
    # print(n, 1)
    arr = [x for x in range(2, n + 1, 2)][::-1]
    # print(n//2, min(arr))
    scale = n // 2
    step = 2
    while scale not in known:
        arr = [arr[k] for k in range(1, len(arr), 2)][::-1]

        scale //= 2
        step *= 2
        # print(scale, min(arr))
    v = arr[known[scale]]
    known[n] = v - 1
    known[n + 1] = v - 1
    return known[n] + 1

# def p(i):
#     if i % 64 == 0:
#         arr = [x for x in range(22, i + 1, 64)]
#     elif i % 32 == 0:
#         arr = [x for x in range(22, i + 1, 32)][::-1]
#     elif i % 16 == 0:
#         arr = [x for x in range(6, i + 1, 16)]
#     elif i % 8 == 0:
#         arr = [x for x in range(6, i + 1, 8)][::-1]
#     elif i % 4 == 0:
#         arr = [x for x in range(2, i + 1, 4)]
#     else:
#         arr = [x for x in range(2, i + 1, 2)][::-1]
#
#     while len(arr) > 1:
#         arr = [arr[k] for k in range(1, len(arr), 2)]
#         arr = arr[::-1]
#
#     return arr[0]


seen = set()
for n in range(2, 10**target, 2):
    r = rec(n)
    if r not in seen:
        print(n, r)
        seen.add(r)
    total += r * 2

print(len(known))
total += rec(10**target)

if target in check:
    # print(total)
    assert total == check[target]
else:
    print(total)
