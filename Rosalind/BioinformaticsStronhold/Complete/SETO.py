# Introduction to Set Operations

with open('../Resources/rosalind_seto.txt', 'r') as file:
    lines = file.readlines()

    n = int(lines[0])
    a = [int(i) for i in lines[1][1:-2].split(', ')]
    b = [int(i) for i in lines[2][1:-2].split(', ')]

# Union
u = {}
for i in a:
    u[i] = 0
for i in b:
    u[i] = 0
print('{' + ', '.join([str(a) for a in u.keys()]) + '}')

# Intersection
i = []
for c in a:
    if c in b:
        i.append(c)
print('{' + ', '.join([str(a) for a in i]) + '}')

# A - B
c = a[:]
for i in b:
    if i in c:
        c.remove(i)
print('{' + ', '.join([str(a) for a in c]) + '}')

# B - A
c = b[:]
for i in a:
    if i in c:
        c.remove(i)
print('{' + ', '.join([str(a) for a in c]) + '}')

# Complement of A
c = [i for i in range(1, n + 1) if i not in a]
print('{' + ', '.join([str(a) for a in c]) + '}')

# Complement of B
c = [i for i in range(1, n + 1) if i not in b]
print('{' + ', '.join([str(a) for a in c]) + '}')
