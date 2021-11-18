# Birthday Memorization

bd = {}

for _ in range(int(input())):
    name, c, d = input().split()
    c = int(c)

    if d in bd:
        if bd[d][1] < c:
            bd[d] = [name, c]
    else:
        bd[d] = [name, c]

print(len(bd))
print('\n'.join(sorted(map(lambda x: x[0], bd.values()))))
