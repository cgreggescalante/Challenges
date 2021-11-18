# Pot

N = int(input())

t = 0

for _ in range(N):
    s = input()
    x = int(s[:-1])
    p = int(s[-1])
    t += x ** p

print(t)
