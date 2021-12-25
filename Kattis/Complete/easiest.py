# The Easiest Problem is This One

n = int(input())

while n:
    a = sum(map(int, str(n)))
    b = -1
    i = 10
    while b != a:
        i += 1
        b = sum(map(int, str(n * i)))
    print(i)

    n = int(input())
