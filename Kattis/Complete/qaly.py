# Quality-Adjusted Life-Year

N = int(input())

s = 0

for _ in range(N):
    a, b = map(float, input().split())
    s += a * b

print(s)
