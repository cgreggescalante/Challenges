# Number Steps

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    if x - y in [0, 2]:
        print(x * 2 - x % 2 - (x - y))
    else:
        print("No Number")

