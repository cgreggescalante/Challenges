# Counting Subsets

n = 861

t = 1

while n > 0:
    t *= 2
    t %= 1000000
    n -= 1

print(t)
