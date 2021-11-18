# Adding Reversed Numbers

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    a = int(str(a)[::-1])
    b = int(str(b)[::-1])

    print(int(str(a + b)[::-1]))
