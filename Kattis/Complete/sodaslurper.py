# Soda Slurper

e, f, c = map(int, input().split())

t = e + f
drank = 0

while t >= c:
    d = t // c
    t %= c
    drank += d
    t += d

print(drank)
