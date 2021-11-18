# Heart Rate

N = int(input())

for _ in range(N):
    b, p = map(float, input().split())

    min_t = p / (b - 1)
    max_t = p / (b + 1)

    print(60 / min_t, b / p * 60, 60 / max_t)
