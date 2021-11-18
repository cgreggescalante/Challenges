# Virtual Friends

t = int(input())

for _ in range(t):
    f = int(input())
    groups = []
    for _ in range(f):
        a, b = input().split()
        if len(groups) == 0:
            groups.append({a, b})
            print(2)
            continue
        i = 0
        while i < len(groups):
            if a in groups[i] or b in groups[i]:
                j = i + 1
                groups[i].add(a)
                groups[i].add(b)
                while j < len(groups):
                    if a in groups[j] or b in groups[j]:
                        groups[i].update(groups.pop(j))
                    else:
                        j += 1
                print(len(groups[i]))
                break
            else:
                i += 1

