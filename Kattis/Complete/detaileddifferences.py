# Detailed Differences

n = int(input())

compare = lambda x: "." if x[0] == x[1] else "*"

for _ in range(n):
    a, b = input(), input()
    print(a)
    print(b)
    print(''.join(compare(v) for v in zip(a, b)))
    print()
