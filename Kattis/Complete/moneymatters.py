# Money Matters

n, m = map(int, input().split())

friends = [int(input()) for _ in range(n)]

idx_sets = [set()]

for _ in range(m):
    a, b = map(int, input().split())
    sets = []
    i = 0
    while i < len(idx_sets):
        if a in idx_sets[i] or b in idx_sets[i]:
            sets.append(idx_sets.pop(i))
        else:
            i += 1
    l = len(sets)
    if l == 0:
        idx_sets.append({a, b})
    elif l == 1:
        sets[0].add(a)
        sets[0].add(b)
        idx_sets.append(sets[0])
    else:
        s = set()
        for i in sets:
            s.update(i)
        idx_sets.append(s)

poss = True
for s in idx_sets:
    sub = [friends[i] for i in s]
    if sum(sub) != 0:
        poss = False
        break

print("POSSIBLE" if poss else "IMPOSSIBLE")
