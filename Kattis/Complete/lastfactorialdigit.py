# Last Factorial Digit

T = int(input())

for _ in range(T):
    n = int(input())

    t = 1
    for i in range(2, n+1):
        t *= i
        t %= 10

    print(t)
