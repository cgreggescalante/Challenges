# Secret Message

N = int(input())

for _ in range(N):
    line = input()
    l = len(line)
    k = 0

    for i in range(1, 101):
        if i * i >= l:
            k = i
            break

    for i in range(k):
        for j in range(k - 1, -1, -1):
            try:
                print(line[i + j * k], end="")
            except IndexError:
                pass
    print()
