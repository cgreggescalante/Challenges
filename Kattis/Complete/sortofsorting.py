# Sort of Sorting

n = int(input())

while n > 0:
    names = [input() for _ in range(n)]
    for name in sorted(names, key=lambda x: x[:2]):
        print(name)
    print()
    n = int(input())
