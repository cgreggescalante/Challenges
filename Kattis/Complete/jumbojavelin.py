# Jumbo Javelin

N = int(input())

s = sum(map(int, [input() for _ in range(N)]))

print(s - N + 1)
