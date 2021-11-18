# Hardware
from collections import defaultdict

n = int(input())

for _ in range(n):
    print(input())
    add = input().split()
    print(add[0], add[1])
    add_count = int(add[0])
    addresses = []

    while len(addresses) < add_count:
        line = input().split()
        if line[0] == "+":
            start, end, step = map(int, line[1:])
            addresses.extend([str(a) for a in range(start, end+1, step)])
        else:
            addresses.append(line[0])

    digits = defaultdict(int)

    for a in addresses:
        for d in a:
            digits[d] += 1

    for i in range(10):
        print(f"Make {digits[str(i)]} digit {i}")

    if sum(digits.values()) > 1:
        print(f"In total {sum(digits.values())} digits")
    else:
        print(f"In total {sum(digits.values())} digit")

