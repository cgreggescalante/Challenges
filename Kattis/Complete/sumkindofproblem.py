# Sum Kind of Problem

p = int(input())

for _ in range(p):
    k, n = map(int, input().split())
    a = (n * (n + 1)) // 2
    b = a * 2 - n
    c = a * 2
    print(k, a, b, c)
