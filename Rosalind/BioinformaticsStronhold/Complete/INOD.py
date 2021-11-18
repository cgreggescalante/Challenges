# Counting Phylogenetic Ancestors

n = 8862
t = 0
while n > 1:
    t += n // 2
    n = n // 2 + n % 2

print(t - 1)