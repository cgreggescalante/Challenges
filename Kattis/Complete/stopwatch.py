# Stopwatch

N = int(input())

if N % 2:
    print("still running")
else:
    t = -sum([int(input()) - int(input()) for _ in range(N // 2)])
    print(t)
